word = input("Ingrese la palabra/frase a enmascarar: ");

enmascarada = "";
if len(word) > 2:
    enmascarada = f'{word[0]}{"*" * len(word[1:-1])}{word[-1]}';
else:
    enmascarada = word;

i = 0
while i < len(word):
    if(word[i]==" "):
        enmascarada = ''.join([*enmascarada[0:(i-1)], " ",*enmascarada[(i+1):]]);
    i += 1
    
print(enmascarada);
