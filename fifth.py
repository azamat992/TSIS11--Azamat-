import psycopg2

def delete_data_by_username_or_phone(search_text):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="JusticeForSaltanat"
    )
    cur = conn.cursor()
    try:
        cur.execute('EXECUTE delete_data_by_username_or_phone(%s)', (search_text,))
        conn.commit()
        print("Data deleted successfully!")
    except psycopg2.DatabaseError as e:
        conn.rollback()
        print("Error:", e)
    cur.close()
    conn.close()

search_text = input("Name: ") 
delete_data_by_username_or_phone(search_text)
