import datetime
import sqlite3

# create a database connection
conn = sqlite3.connect('hours.db')

# create a table to store hours
conn.execute('''CREATE TABLE IF NOT EXISTS hours
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT NOT NULL,
              start_time TEXT NOT NULL,
              end_time TEXT NOT NULL,
              notes TEXT)''')

# function to add hours to the database
def add_hours(start_time, end_time, notes):
    date = datetime.date.today()
    conn.execute("INSERT INTO hours (date, start_time, end_time, notes) VALUES (?, ?, ?, ?)",
                 (date, start_time, end_time, notes))
    conn.commit()

# function to retrieve hours from the database
def get_hours():
    cursor = conn.execute("SELECT * FROM hours")
    rows = cursor.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("Date = ", row[1])
        print("Start Time = ", row[2])
        print("End Time = ", row[3])
        print("Notes = ", row[4])

# prompt the user to enter start and end times and notes
start_time = input("Enter start time (HH:MM): ")
end_time = input("Enter end time (HH:MM): ")
notes = input("Enter notes: ")

# add hours to the database
add_hours(start_time, end_time, notes)

# retrieve hours from the database
get_hours()

# close the database connection
conn.close()
