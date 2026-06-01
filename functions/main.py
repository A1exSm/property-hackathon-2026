from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os
from pydantic import BaseModel

app = FastAPI()

# Database configuration
DB_HOST = os.getenv("DB_HOST") # Your Cloud SQL IP
DB_USER = os.getenv("DB_USER") # MySQL username
DB_PASSWORD = os.getenv("DB_PASSWORD") # MySQL password
DB_PORT = os.getenv("DB_PORT") # Default MySQL port

# Connection string (MySQL + PyMySQL)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

# Create SQLAlchemy engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True
)

class Response(BaseModel):
    success: bool
    message: str
    created: bool = False

@app.get("/create-database", response_model=Response)
async def create_db():
    try:
        with engine.connect() as connection:
            # Fixed query syntax
            result = connection.execute(text("SHOW DATABASES LIKE 'Properties_Telemetry'"))
            exists = result.scalar() is not None

            if not exists:
                connection.execute(text("CREATE DATABASE Properties_Telemetry"))
                connection.execute(text("USE Properties_Telemetry"))
                connection.commit()
                return {
                    "success": True,
                    "message": "Database created successfully",
                    "created": True
                }
            else:
                connection.execute(text("USE Properties_Telemetry"))
                return {
                    "success": True,
                    "message": "Database already exists",
                    "created": False
                }
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
