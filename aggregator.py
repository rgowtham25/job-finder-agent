from fetchers.linkedin import fetch_linkedin_jobs
from filters import role_match, location_match, duration_match, deduplicate

def get_jobs(role, location, duration_days):
    print("DEBUG: get_jobs() started")

    jobs = fetch_linkedin_jobs(role, location)

    filtered = [
        job for job in jobs
        if role_match(job)
        and duration_match(job, duration_days)
    ]

    return deduplicate(filtered)
