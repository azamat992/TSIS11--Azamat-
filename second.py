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

# Define the function to insert/update a user
def insert_update_user(person_name, phone_number):
    try:
        # Execute the stored procedure using the EXECUTE statement
        cur.execute('EXECUTE insert_update_user(%s, %s)', (person_name, phone_number))
        # Commit the transaction
        conn.commit()
        print("User inserted/updated successfully!")
    except psycopg2.DatabaseError as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        print("Error:", e)

# Example usage
name = input("Enter name: ")
number = input("Enter phone number: ")
insert_update_user(name, number)

# Close cursor and connection
cur.close()
conn.close()
