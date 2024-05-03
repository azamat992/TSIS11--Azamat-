import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="JusticeForSaltanat"
)

cur = conn.cursor()

cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_update_user(person_name TEXT, phone_number TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS(SELECT 1 FROM your_table WHERE name = person_name) THEN
            UPDATE your_table SET phone = phone_number WHERE name = person_name;
            RAISE NOTICE 'User % updated with phone number %', person_name, phone_number;
        ELSE
            INSERT INTO your_table (name, phone) VALUES (person_name, phone_number);
            RAISE NOTICE 'New user % added with phone number %', person_name, phone_number;
        END IF;
    END;
    $$;
""")

conn.commit()

def insert_update_user(person_name, phone_number):
    try:
        cur.callproc('insert_update_user', (person_name, phone_number))
        conn.commit()
        print("User inserted/updated successfully!")
    except psycopg2.DatabaseError as e:
        conn.rollback()
        print("Error:", e)

name = input("Enter name: ")
number = input("Enter phone number: ")
insert_update_user(name, number)

cur.close()
conn.close()
