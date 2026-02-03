from app.db import get_connection

def add_job(title, company, location):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO jobs (title, company, location) VALUES (?, ?, ?)",
        (title, company, location)
    )
    conn.commit()
    conn.close()

def delete_job(job_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()

def list_jobs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, company, location FROM jobs")
    rows = cur.fetchall()
    conn.close()

    jobs = []
    for row in rows:
        jobs.append({
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3]
        })

    return jobs

def get_job_by_id(job_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, title, company, location FROM jobs WHERE id = ?",
        (job_id,)
    )
    row = cur.fetchone()
    conn.close()

    if row is None:
        return None
    
    return {
        "id": row[0],
        "titile": row[1],
        "company": row[2],
        "location": row[3]
    }

def update_job(job_id, title, company, location):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE jobs
        SET title = ?, company = ?, location = ?
        WHERE id = ?
    """, (title, company, location, job_id))

    if cursor.rowcount == 0:
        conn.close()
        return {"error": "Job not found"}

    conn.commit()
    conn.close()

    return {"status": "Job updated successfully"}

