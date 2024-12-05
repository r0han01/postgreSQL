import psycopg2

# Define connection parameters (this only needs to be done once)
host = "localhost"
port = 5432
dbname = "postgres"
user = "postgres"
password = "mysecretpassword"

def get_connection():
    """Establish a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

def create_table():
    """Create a 'Customers' table in the PostgreSQL database."""
    try:
        # Establish connection to the database
        connection = get_connection()
        cursor = connection.cursor()

        # SQL query to create the table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID SERIAL PRIMARY KEY,
            FirstName VARCHAR(100),
            LastName VARCHAR(100),
            Email VARCHAR(100),
            DateOfBirth DATE
        );
        """
        # Execute the query to create the table
        cursor.execute(create_table_query)
        connection.commit()  # Commit the changes
        print("Customers table created successfully")

    except Exception as error:
        print("Error while creating table:", error)

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

# Run the function to create the table
if __name__ == "__main__":
    create_table()
