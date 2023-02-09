import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I have good game for u!")


if __name__ == '__main__':
    application = ApplicationBuilder().token('6279724653:AAGu3_RuSco7bV_XLFq14u8PE-9to5fxOIM').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()