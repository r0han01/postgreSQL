# PostgreSQL Operations with Python

This repository contains a Python application that demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database using the `psycopg2` library.

## Requirements

- Python 3.x
- PostgreSQL Database
- psycopg2 library (Install via `pip install psycopg2`)

## Setup and Configuration

Before running the script, make sure you have a PostgreSQL database instance running. You will also need to configure the connection parameters in the code.

### Connection Setup

The connection to the PostgreSQL database is established using the `psycopg2` library. The connection parameters are as follows:

- **Host**: `localhost` (or your PostgreSQL server)
- **Port**: `5432` (default PostgreSQL port)
- **Database Name**: `postgres` (or your specific database name)
- **User**: `postgres` (or your PostgreSQL user)
- **Password**: Your PostgreSQL user's password

Example:
```python
host = "localhost"
port = 5432
dbname = "postgres"
user = "postgres"
password = "yourpassword"
