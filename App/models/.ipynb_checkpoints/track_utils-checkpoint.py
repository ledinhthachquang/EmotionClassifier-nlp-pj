# Load Database Pkg
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create Page Visited Table
def create_page_visited_table():
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT,timeOfvisit TIMESTAMP)')

# Create Emotion Classifier Table
def create_emotionclf_table():
    c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')

# Create Tables
create_page_visited_table()
create_emotionclf_table()

# Close Connection
conn.close()
