from fastapi import FastAPI, HTTPException
from app.crud import add_job, delete_job, list_jobs, update_job, get_job_by_id
from app.schemas import JobCreate, JobResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SQL Inventory API is running"}

@app.post("/jobs/", response_model=JobResponse)
def create_job(job: JobCreate):
    job_id = add_job(job.title, job.company, job.location)
    return {
        "id": job_id,
        "title": job.title,
        "company": job.company,
        "location": job.location
    }

@app.get("/jobs", response_model=list[JobResponse])
def get_all_jobs():
    return list_jobs()

@app.delete("/jobs/{job_id}")
def remove_job(job_id: int):
    delete_job(job_id)
    return {"status": "Job deleted successfully"}

@app.put("/jobs/{job_id}")
def edit_job(
    job_id: int, 
    title: str, 
    company: str, 
    location: str
):
    return update_job(job_id, title, company, location)

@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int):
    job = get_job_by_id(job_id)
    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )
    return job