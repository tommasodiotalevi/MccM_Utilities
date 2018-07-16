import sqlite3
connection = sqlite3.connect("higgsEXO.db")

cursor = connection.cursor()

# delete 
#cursor.execute("""DROP TABLE employee;""")

sql_command = """
CREATE TABLE request ( 
request_id INTEGER PRIMARY KEY, 
name VARCHAR(40), 
condition VARCHAR(40), 
chain VARCHAR(256), 
number_requests INTEGER,
number_events   INTEGER, 
creation DATE,
status VARCHAR(30));"""

cursor.execute(sql_command)

sql_command_tab2 = """
CREATE TABLE McM_Entry (
id INTEGER PRIMARY KEY,
request_id INTEGER,
prepID VARCHAR(40),
dataset_name VARCHAR(256),
number_events INTEGER,
gridpack  VARCHAR(512),
status  VARCHAR(30)
);"""

cursor.execute(sql_command_tab2)


