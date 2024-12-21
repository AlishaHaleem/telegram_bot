from typing import Final

from Tools.scripts.fixheader import process
from telegram import Update
from telegram.ext import (Application ,ContextTypes
,CommandHandler ,MessageHandler ,filters)

TOKEN :Final =  '7729568993:AAHbGYLsyNPTUPMKV2kitkmbW3oVS8VjMVo'
USERNAME_BOT : Final = '@bbbjohnbot'
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me'
                                    '.I am John your AI doctor!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am John ! Please try something so i can respond!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Handle responses
def handle_response(text: str)-> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Hey there !'
    if 'how are you' in processed:
        return 'I am fine !'
    if 'i am fine' in processed:
        return 'Great !'
    return 'Try asking something else!'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str = update.message.text
    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if USERNAME_BOT in text:
            new_text: str = text.replace(USERNAME_BOT, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)


    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot......')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

# Message handler
    app.add_handler(MessageHandler(filters.TEXT , handle_message))
# Error handler
    app.add_error_handler(error)

# Polls the bot
    print('up and running...')
    app.run_polling(poll_interval=3)