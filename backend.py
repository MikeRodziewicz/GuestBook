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
    return rows
