from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import functions_for_sql as sql
from pathlib import Path
import text_parsing as t_p
import logger

file_name = "telephone_directory.sqlite"
relative_file_directory = Path(file_name)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)

    text1 = "/find_by_name -> найти запись по имени\n"
    text2 = "Пример: /find_by_name Федор\n"
    text3 = "/find_by_surname -> найти запись по фамилии\n"
    text4 = "Пример: /find_by_surname Санников\n"
    text5 = "/find_by_name_and_surname -> найти запись по имени и фамилии\n"
    text6 = "Пример: /find_by_name_and_surname Федор Санников\n"
    text7 = "/find_by_phone_number -> найти запись по номеру телефона\n"
    text8 = "Пример: /find_by_phone_number 620070 \n"
    text9 = "/show_all_record -> вывести все записи в справочнике (подумай стоит ли это делать) \n"
    await update.message.reply_text(f'{text1+text2+text3+text4+text5+text6+text7+text8+text9}')

async def find_by_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)
    global relative_file_directory      
    message = str(update.message.text)
    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_name")
    sql_request = "SELECT people.name, people.surname, phones.phone_number FROM people LEFT JOIN phones ON people.id = people_id WHERE name = '{}'".format(message)
    connection = sql.create_connection(relative_file_directory)
    ansver_sql = sql.execute_read_query(connection, sql_request)
    ansver = t_p.print_answer_for_bot_v1(ansver_sql)
    await update.message.reply_text(ansver)

async def find_by_surname(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)    
    global relative_file_directory    
    message = str(update.message.text)
    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_surname")
    sql_request = "SELECT people.name, people.surname, phones.phone_number FROM people LEFT JOIN phones ON people.id = people_id WHERE surname = '{}'".format(message)
    connection = sql.create_connection(relative_file_directory)
    ansver_sql = sql.execute_read_query(connection, sql_request)
    ansver = t_p.print_answer_for_bot_v1(ansver_sql)
    await update.message.reply_text(ansver)

async def find_by_name_and_surname(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)
    global relative_file_directory    
    message = str(update.message.text)
    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_name_and_surname")
    message = message.split(" ")
    sql_request = "SELECT people.name, people.surname, phones.phone_number FROM people, phones WHERE people.id = people_id AND name = '{}' AND surname = '{}'".format(message[0], message[1])    
    connection = sql.create_connection(relative_file_directory)
    ansver_sql = sql.execute_read_query(connection, sql_request)
    ansver = t_p.print_answer_for_bot_v1(ansver_sql)
    await update.message.reply_text(ansver)

async def find_by_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)
    global relative_file_directory 
    message = str(update.message.text)
    message = t_p.clearing_line_from_bot_telegrams(message, "/find_by_phone_number")
    sql_search_request = "SELECT people.name, people.surname, phones.phone_number FROM phones INNER JOIN people ON phones.people_id = people.id WHERE phone_number = '{}'".format(message)    
    connection = sql.create_connection(relative_file_directory)    
    ansver_sql = sql.execute_read_query(connection, sql_search_request)
    ansver = t_p.print_answer_for_bot_v1(ansver_sql)
    await update.message.reply_text(ansver)

async def show_all_record(update: Update, context: ContextTypes.DEFAULT_TYPE):

    logger.record_keeping(update)
    global relative_file_directory    
    sql_search_request = "SELECT people.name, people.surname, phones.phone_number FROM phones INNER JOIN people ON people.id = phones.people_id"
    connection = sql.create_connection(relative_file_directory)
    ansver_sql = sql.execute_read_query(connection, sql_search_request)
    ansver = t_p.print_answer_for_bot_v1(ansver_sql)
    await update.message.reply_text(ansver)