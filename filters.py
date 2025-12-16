from config import ROLE_KEYWORDS, LOCATION_ALIASES
from time_utils import posted_text_to_days

def role_match(job):
    title = job.title.lower()
    return any(keyword in title for keyword in ROLE_KEYWORDS)

def location_match(job, location):
    text = (job.title + " " + job.company).lower()
    return any(loc in text for loc in LOCATION_ALIASES)

def duration_match(job, max_days):
    days = posted_text_to_days(job.posted)
    if days is None:
        return True
    return days <= max_days


def deduplicate(jobs):
    seen = set()
    unique = []

    for job in jobs:
        print(job.posted)
        key = (job.company.lower(), job.title.lower())
        if key not in seen:
            seen.add(key)
            unique.append(job)

    return unique
