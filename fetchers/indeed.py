import requests
from bs4 import BeautifulSoup
from config import HEADERS
from models import Job

def fetch_indeed_jobs(role: str, location: str, days: int) -> list[Job]:
    url = (
        f"https://in.indeed.com/jobs"
        f"?q={role}&l={location}&fromage={days}"
    )

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for card in soup.select("a.tapItem"):
        title_el = card.select_one("h2 span")
        company_el = card.select_one("span.companyName")

        if not (title_el and company_el):
            continue

        link = "https://in.indeed.com" + card.get("href")

        jobs.append(Job(
            title=title_el.text.strip(),
            company=company_el.text.strip(),
            link=link,
            source="Indeed"
        ))

    return jobs
