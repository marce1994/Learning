import requests
import json
import os
import re

def get_word(word):
    print("Searching", word);
    res_path = f'words/{word}.json';
    res_audio_path = f'audio/{word}.mp3';

    exists = os.path.isfile(res_path);
    
    if exists is True:
        with open(res_path, "r") as read_file:
            print(f'Loading {word} from file {res_path}')
            result = json.load(read_file);
    else:
        print(f'Loading {word} from external service');
        
        response = requests.get("https://tuna.thesaurus.com/pageData/" + word);

        if response.status_code >= 300 or response.text == '{"data":null}':
            print(f"No encontrado {response.status_code}");
            result = None;
        else:
            print(response.text);
            result = json.loads(response.text)

    if result is None:
        return (
            False,
            word,
            [],
            [],
            None,
            None,
            None
        );
    else:
        synonyms_dic = result["data"]["definitionData"]["definitions"][0]["synonyms"];
        antonyms_dic = result["data"]["definitionData"]["definitions"][0]["antonyms"];
        word = result["data"]["definitionData"]["entry"];
        pronuntiation = cleanhtml(result["data"]["pronunciation"]["spell"]);
        mp3_url = result["data"]["pronunciation"]["audio"]["audio/mpeg"];

        exists = os.path.isfile(res_audio_path);
        
        if exists is True:
            with open(res_audio_path, "rb") as read_file:
                print(f'Loading {word} audio from file {res_audio_path}')
                mp3 = read_file.read();
        else:
            print(f'Loading {word} audio from external service');
            mp3 = requests.get(mp3_url).content;
        
        meaning = result["data"]["definitionData"]["definitions"][0]["definition"];
        synonyms = list(map(lambda x: x["term"], filter(lambda x: x["similarity"] == "100", synonyms_dic)));
        antonyms = list(map(lambda x: x["term"], filter(lambda x: x["similarity"] == "-100", antonyms_dic)));
        
        with open(res_path, "w") as write_file:
            json.dump(result, write_file);
        with open(res_audio_path, "wb") as write_file:
            write_file.write(mp3);

        return (
            True,
            word,
            synonyms[0:4],
            antonyms[0:4],
            meaning,
            pronuntiation,
            mp3
        );


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext