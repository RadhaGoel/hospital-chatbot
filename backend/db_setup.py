import sqlite3

conn = sqlite3.connect("backend/hospital.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    available_time TEXT
)
""")

# Clear old data (important for re-run)
cursor.execute("DELETE FROM doctors")

# Insert mock data
cursor.executemany("""
INSERT INTO doctors (name, specialization, available_time)
VALUES (?, ?, ?)
""", [
    ("Dr. Sharma", "General Physician", "5 PM - 8 PM"),
    ("Dr. Mehta", "Cardiologist", "10 AM - 2 PM"),
    ("Dr. Khan", "Neurologist", "1 PM - 4 PM"),
    ("Dr. Gupta", "Dermatologist", "11 AM - 3 PM"),
])

conn.commit()
conn.close()

print("✅ Database created with doctors data")