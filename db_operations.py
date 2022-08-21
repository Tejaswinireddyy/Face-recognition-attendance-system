import csv
from collections import Counter
import mysql.connector
from datetime import date

present = []
seen = set()
counts = Counter(row[0] for row in present)
present = [row for row in present if row[0] not in seen and not seen.add(row[0])]

# Database operations

# CSV contents in memory
with open('Attendance.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        present.append(tuple([row[0], row[1]]))

# Unique person records
try:
    conn_object = mysql.connector.connect(host="localhost", user="root", password="", database="attendance")

    cursor = conn_object.cursor()
    date = date.today().strftime("%d/%m/%Y")
    for r in present:
        query = "INSERT INTO attendance_status(date, name, time) VALUES ('"+date+"','"+ r[0]+"','"+ r[1]+"')"
        print(query)
        cursor.execute(query)
        conn_object.commit()
    conn_object.close

except:
    print("Database connection exception!")
