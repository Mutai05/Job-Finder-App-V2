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

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.mappings():
            jobs.append(dict(row))
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}
        )
        row = result.mappings().first()
        if row is None:
            return None
        else:
            return dict(row)
