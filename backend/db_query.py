import sqlite3

def get_all_doctors():
    conn = sqlite3.connect("backend/hospital.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, specialization, available_time FROM doctors")
    results = cursor.fetchall()

    conn.close()
    return results


def get_doctors_by_specialization(spec):
    conn = sqlite3.connect("backend/hospital.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, available_time FROM doctors
    WHERE specialization LIKE ?
    """, ('%' + spec + '%',))

    results = cursor.fetchall()

    conn.close()
    return results