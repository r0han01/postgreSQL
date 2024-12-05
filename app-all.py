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

# Example 1: Create a Table
def create_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID SERIAL PRIMARY KEY,
            FirstName VARCHAR(100),
            LastName VARCHAR(100),
            Email VARCHAR(100),
            DateOfBirth DATE
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Customers table created successfully")

    except Exception as error:
        print("Error while creating table:", error)

    finally:
        cursor.close()
        connection.close()

# Example 2: Insert Data into the Table
def insert_data():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Customers (FirstName, LastName, Email, DateOfBirth)
        VALUES (%s, %s, %s, %s)
        """
        customer_data = ('John', 'Doe', 'john.doe@example.com', '1985-04-25')
        cursor.execute(insert_query, customer_data)
        connection.commit()
        print("Customer inserted successfully")

    except Exception as error:
        print("Error while inserting data:", error)

    finally:
        cursor.close()
        connection.close()

# Example 3: Query Data from the Table
def query_data():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Customers;"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        print("Customers in the database:")
        for row in rows:
            print(row)

    except Exception as error:
        print("Error while querying data:", error)

    finally:
        cursor.close()
        connection.close()

# Example 4: Update a Record
def update_data():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
        UPDATE Customers
        SET Email = %s
        WHERE CustomerID = %s;
        """
        new_email = 'john.doe.updated@example.com'
        customer_id = 1
        cursor.execute(update_query, (new_email, customer_id))
        connection.commit()
        print("Customer's email updated successfully")

    except Exception as error:
        print("Error while updating data:", error)

    finally:
        cursor.close()
        connection.close()

# Example 5: Delete a Record
def delete_data():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = "DELETE FROM Customers WHERE CustomerID = %s;"
        customer_id = 1
        cursor.execute(delete_query, (customer_id,))
        connection.commit()
        print("Customer deleted successfully")

    except Exception as error:
        print("Error while deleting data:", error)

    finally:
        cursor.close()
        connection.close()

# Example usage of the functions
if __name__ == "__main__":
     create_table()
     insert_data()
     query_data()
     update_data()
     delete_data()
