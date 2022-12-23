from telegram import Update
import functions_for_sql as sql
from pathlib import Path
import datetime

file_name = "database_logger.sqlite"
relative_file_directory = Path(file_name)

def record_keeping(update: Update):
    
    global relative_file_directory
    
    d_t_n = datetime.datetime.now()

    data_and_time_str =str(d_t_n.day) + "." + str(d_t_n.month) + "." + str(d_t_n.year) \
        + " " + str(d_t_n.hour) + ":" + str(d_t_n.minute) + ":" + str(d_t_n.second)
    
    connection = sql.create_connection(relative_file_directory)

    input_data = "INSERT INTO log_command (data_and_time_message, user_first_name, user_id, user_message_text) VALUES ('{}','{}','{}','{}')"\
        .format(data_and_time_str,str(update.effective_user.first_name),str(update.effective_user.id),str(update.message.text))
    
    sql.execute_query(connection, input_data)