import datetime
import mysql.connector
import random
import time

mysql_conf = {
    "user": "",
    "password": "",
    "host": "localhost",
    "database": "citizenwatt",
    "raise_on_warnings": True,
    "autocommit": True
}

bdd = mysql.connector.connect(**mysql_conf)
bdd_cursor = bdd.cursor()

while True:
    query = ("INSERT INTO measures(date, power) VALUES(%s, %s)")
    values = (datetime.datetime.now(), random.randint(1, 3500))
    bdd_cursor.execute(query, values)
    print(values)
    time.sleep(2)
