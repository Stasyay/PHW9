from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pathlib import Path
import bot_commands as bot_com

file_name = "token.config"
relative_file_directory = Path(file_name)

with open(relative_file_directory, 'r') as data:
    my_token = data.read().replace('\n', '')

def start_talking_bot_with_people():
    
    app = ApplicationBuilder().token(my_token).build()
    
    app.add_handler(CommandHandler("help", bot_com.help_command))
    app.add_handler(CommandHandler("find_by_name", bot_com.find_by_name))
    app.add_handler(CommandHandler("find_by_surname", bot_com.find_by_surname))
    app.add_handler(CommandHandler("find_by_name_and_surname", bot_com.find_by_name_and_surname))
    app.add_handler(CommandHandler("find_by_phone_number", bot_com.find_by_phone_number))
    app.add_handler(CommandHandler("show_all_record", bot_com.show_all_record))

    print("server start")
    app.run_polling()