from db import get_connection

def add_job(title, company, location):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO jobs (title, company, location) VALUES (?, ?, ?)",
        (title, company, location)
    )

    conn.commit()
    conn.close()
    print("Job added successfully")

def delete_job(job_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM jobs WHERE id = ?", (job_id,))

    conn.commit()
    conn.close()
    print("Job deleted successsfully")

def update_job_location(job_id, new_location):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE jobs SET location = ? WHERE id = ?",
        (new_location, job_id)
    )

    conn.commit()
    conn.close()
    print("Job updated successfully")

def list_jobs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM jobs")
    rows = cur.fetchall()
    conn.close()
    return rows
