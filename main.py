import logging 

from telegram.ext import Updater, CommandHandler 


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


updater = Updater(
    token='1357858620:AAEBE0cjYb6Z1FkkRgNHMixT1MmFiAnyKNk'
)
dispatcher = updater.dispatcher

def start(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Hello world!",
    )

start_handler = CommandHandler(
    'start' , start
)

dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    updater.start_polling()