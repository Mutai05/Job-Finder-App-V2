from sqlalchemy import create_engine, text


# Updated connection string with root user credentials
db_connection_string = "mysql+pymysql://mutaikelvin:Kipkemboi@localhost/jobfinderweb?charset=utf8mb4"

# Create the SQLAlchemy engine
engine = create_engine(db_connection_string)

try:
    # Connect to the database
    with engine.connect() as conn:
        # Execute a simple query to test the connection
        result = conn.execute(text("SELECT * FROM jobs"))

        # Print the results
        for row in result:
            print(row)
except sqlalchemy.exc.OperationalError as e:
    print("Operational error connecting to the database:", e)
except sqlalchemy.exc.ProgrammingError as e:
    print("Programming error executing SQL query:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
