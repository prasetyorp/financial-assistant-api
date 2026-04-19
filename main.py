from fastapi import FastAPI, Request
import psycopg2
import os



app = FastAPI()

# 🔹 DB connection function
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),  # e.g., "db.xtotgobiapzsupkydvpc.supabase.co"
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME"),  # e.g., "postgres"
        user=os.getenv("DB_USER"),  # e.g., "postgres"
        password=os.getenv("DB_PASSWORD"),
        sslmode="require",
        options="-c search_path=ryanhanna"
    )

# 🔹 Test endpoint
@app.get("/test-db")
def test_db():
    try:
        conn = get_connection()
        conn.close()
        return {"status": "DB connected ✅"}
    except Exception as e:
        return {"error": str(e)}

# 🔹 Root endpoint
@app.get("/")
def root():
    return {"message": "API is running 🚀"}