import sqlite3

#creating table 
def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS BLOG_DETAILS (TITLE TEXT, DESCRIPTION TEXT)")
    print('\nTable created succesfully\n')
    conn.close()
    
#inserting values
def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    insert_sql="INSERT INTO BLOG_DETAILS (TITLE, DESCRIPTION) VALUES (?,?)"
    conn.execute(insert_sql,values)
    conn.commit()
    conn.close()

#Retriving and printing values
def get_blog_info(dbname):
    conn = sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM BLOG_DETAILS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()
    
