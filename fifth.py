import psycopg2

# Establish connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="JusticeForSaltanat"
)

# Create a cursor object
cur = conn.cursor()

# Define the function to delete data by username or phone
def delete_data_by_username_or_phone(search_text):
    try:
        # Execute the stored procedure using the EXECUTE statement
        cur.execute('EXECUTE delete_data_by_username_or_phone(%s)', (search_text,))
        conn.commit()
        print("Data deleted successfully!")
    except psycopg2.DatabaseError as e:
        conn.rollback()
        print("Error:", e)

# Example usage
search_text = input("Name: ") # Username or phone number to delete
delete_data_by_username_or_phone(search_text)

# Close cursor and connection
cur.close()
conn.close()
