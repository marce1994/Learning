from thesaurus.thesaurus import get_word
import schedule
import re
# https://irazasyed.github.io/telegram-bot-sdk/usage/keyboards/
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

commands = {
    '/w + word': 'Will tell you information about that word.',
    '/help': 'I will help you, if I can.'
};

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        "<b>Shut up!</b>" +
        "\nWelcome to the classroom." +
        "\nTake notes about the following commands." +
        "\n" +
        "\n".join(list(map(lambda x: f'{x[0]}, {x[1]}', list(commands.items()))))
        , parse_mode='HTML'
    );

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "So, you are coming again asking for help? Well, that's not a surprise of course."
        "\nHere you have some basic commands.\n" +
        "\n".join(list(map(lambda x: f'{x[0]}, {x[1]}', list(commands.items()))))
        , parse_mode='HTML');

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("That's not a command dude!");

def word(update, context):
    """Log Errors caused by Updates."""
    word = re.sub('/[a-zA-Z]\s', '', update.message.text);
    success, word, synonyms, antonyms, meaning, pronunciation, mp3 = get_word(word);

    if success is False:
        update.message.reply_text("Thats not a word!", parse_mode='HTML');
        return;

    print(success, word, synonyms, antonyms);

    message = f'<b>{ word }</b> ({pronunciation})';
    message += f'\nmeaning: {meaning}';
    
    if len(synonyms) != 0:
        message += f'\nSynonyms\n<pre>{ ", ".join(synonyms) }</pre>';
    if len(antonyms) != 0:
        message += f'\nAntonyms\n<pre>{ ", ".join(antonyms) }</pre>';

    update.message.reply_text(message, parse_mode='HTML');
    update.message.reply_voice(mp3);
    
    if update.message.chat_id != 623105152:
        message = f'{update.message.chat_id} {update.message.chat.first_name} {update.message.chat.last_name} searched: {word}';
        update.message.bot.send_message('623105152', message, parse_mode='HTML');

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("BOT_API_KEY", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler("w", word))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()