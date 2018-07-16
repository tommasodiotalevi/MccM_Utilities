import sqlite3
connection = sqlite3.connect("higgsEXO.db")

cursor = connection.cursor()

request_data = [ ("Rizzi_DYVBFFilterd", "94X_Fall17", 2, 20000000, "2018-06-07"),
                 ("Tanvi_SUSYGluGluToHToAA_AToGG", "94X_Fall17", 13, 2600000,"2018-06-07") ]
               
for p in request_data:
    format_str = """INSERT INTO request (request_id, name, condition, number_requests, number_events, creation)
    VALUES (NULL, "{name}", "{cond}", "{num_req}", "{num_evts}", "{creationdate}");"""

    sql_command = format_str.format(name=p[0], cond=p[1], num_req=p[2], num_evts = p[3], creationdate = p[4])
    print(sql_command)
    cursor.execute(sql_command)
connection.commit()
connection.close()
