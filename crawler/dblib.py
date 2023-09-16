import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql = ''' CREATE TABLE dns_domains(
       domain text) '''
    cur = conn.cursor()
    cur.execute(sql)
    sql = ''' CREATE UNIQUE INDEX IF NOT EXISTS index_domain ON dns_domains (domain) '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def create_record(conn, record):
    sql = ''' INSERT OR REPLACE INTO dns_domains(domain)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()
    return cur.lastrowid
