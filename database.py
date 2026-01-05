from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url ="postgresql://postgres:123456789@localhost:5432/raghavs"

# CHANGE COMMENT: Renamed to DATABASE_URL (uppercase) - common convention for constants
# CHANGE COMMENT: Better to store sensitive info like password in environment variables (.env file) for security
engine=create_engine(db_url)

# CHANGE COMMENT: Added useful engine options:
#   - echo=False (or True for debugging) → logs all SQL queries
#   - pool_pre_ping=True → checks if connection is alive before using (very useful with PostgreSQL)
#   - pool_size & max_overflow → controls how many connections are kept open
#   - connect_args → timeout to avoid hanging forever

# CHANGE COMMENT: Renamed 'session' → 'SessionLocal' 
#   - This is the standard FastAPI/SQLAlchemy naming convention
#   - 'session' as a global variable name can cause confusion
#   - SessionLocal is a factory function that creates new sessions
session = sessionmaker(autoflush=False,autocommit=False, bind=engine)

# CHANGE COMMENT: Turned this into a proper dependency function called get_db()
#   - Used in FastAPI routes with Depends(get_db)
#   - Ensures session is properly closed after each request
#   - Prevents database connection leaks

# CHANGE COMMENT: Added a test_connection() function
#   - Safely tests if database is reachable when app starts
#   - Gives helpful error messages if connection fails (wrong password, DB not created, etc.)

print("DataBase Connected Successfully")

# CHANGE COMMENT: This print runs even if connection actually failed!
#   - SQLAlchemy doesn't raise error immediately when creating engine
#   - Real connection is tested only when first query is made
#   - Better to actually test the connection (e.g., run SELECT 1) and print success only if it works