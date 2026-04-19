from fastapi import FastAPI, Request
import psycopg2
import os



app = FastAPI()

# 🔹 DB connection function
def get_connection():
    return psycopg2.connect(
        os.getenv("DB_URL"),
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