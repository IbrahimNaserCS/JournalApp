from datetime import datetime
import sqlite3

# Function to print out database, use strictly for debugging purposes
def displaydb():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT rowid FROM notes")
    print(c.fetchall())

# Adding a note
def adddb(note):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    time = datetime.today().strftime('%Y-%m-%d')
    c.execute("INSERT INTO notes VALUES (?, ?)", (time, note))
    conn.commit()
    conn.close()

# Loading the database as a list of tuples
def loaddb():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()
    return notes

# Deleting a note from the database
def deldb(note):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE note = ?", (note, ))
    conn.commit()
    conn.close()

# Returns the length of the database
def lendb():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT count (*) from notes")
    lenth = c.fetchone()[0]
    conn.close()
    return lenth
