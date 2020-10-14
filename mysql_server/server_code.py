import mysql.connector
from datetime import date
import datetime

db= mysql.connector.connect(
    host='',
    user=''m
    passwd='',
    )

mycursor = db.cursor()
mycursor.execute('SHOW DATAVASES')
