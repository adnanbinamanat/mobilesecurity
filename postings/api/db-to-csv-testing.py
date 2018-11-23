"""
import sqlite3
import csv
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT postings_apipost.Length, postings_apipost.AbsoluteLength, postings_apipost.AvgSpeed, postings_apipost.StartPressure, postings_apipost.EndPressure,  postings_apipost.AvgPressure, postings_apipost.StartSize, postings_apipost.EndSize,  postings_apipost.AvgSize, postings_apipost.StartX, postings_apipost.EndX, postings_apipost.StartY, postings_apipost.EndY, postings_apipost.Area, postings_apipost.Area, postings_apipost.MoveType, postings_apipost.UserID FROM postings_apipost;")
results = cursor.fetchall()
with open("out.csv", "w", newline='') as csv_file:              # Python 3 version
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
    csv_writer.writerows(results)
cursor.close()
connection.close()
"""
# generic
