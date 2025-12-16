from aggregator import get_jobs

if __name__ == "__main__":
    ROLE = "Python Developer"
    LOCATION = "Bangalore"
    DURATION_DAYS = 15

    jobs = get_jobs(ROLE, LOCATION, DURATION_DAYS)

    print(f"\nTotal matched jobs: {len(jobs)}\n")

    for idx, job in enumerate(jobs, start=1):
        print(f"{idx}. {job.company}")
        print(job.title)
        print(f"Posted: {job.posted}")
        print(job.link)
        print("-" * 60)
