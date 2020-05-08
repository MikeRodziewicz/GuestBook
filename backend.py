# **Guestbook / Journal** - A simple application that allows people to add
# comments or write journal entries. It can allow comments or
# not and timestamps for all entries.
#  Could also be made into a shout box.
#  *Optional: Deploy it on Google App Engine or Heroku or any other PaaS
#  (if possible, of course).*


import psycopg2
from datetime import datetime


def connect():
    conn = psycopg2.connect(
        "dbname='GuestBook' user='postgres' password='password123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS guests (name TEXT, comment TEXT, date TIMESTAMP)")
    conn.commit()
    conn.close()


def insert(name, comment, date):
    conn = psycopg2.connect(
        "dbname='GuestBook' user='postgres' password='password123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO guests VALUES (%s,%s,%s)", (name, comment, date))
    conn.commit()
    conn.close()

 def view():
    conn = psycopg2.connect(
        "dbname='GuestBook' user='postgres' password='password123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM guests")
    rows = cur.fetchall()
    conn.close()
    return} rows
