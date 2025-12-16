from playwright.sync_api import sync_playwright
from models import Job

def fetch_linkedin_jobs(role, location):
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = (
            f"https://www.linkedin.com/jobs/search/"
            f"?keywords={role}&location={location}"
        )

        page.goto(url, timeout=60000)
        page.wait_for_selector("div.base-card", timeout=20000)

        # Robust scrolling (container + window fallback)
        job_list = (
            page.query_selector("div.jobs-search-results-list")
            or page.query_selector("div.scaffold-layout__list")
            or page.query_selector("div.scaffold-layout__list-container")
        )

        if job_list:
            print("Scrolling job list container")
            for _ in range(10):
                page.evaluate(
                    "(el) => el.scrollBy(0, el.scrollHeight)",
                    job_list
                )
                page.wait_for_timeout(2000)
        else:
            print("Scrolling window (fallback)")
            for _ in range(10):
                page.evaluate(
                    "window.scrollBy(0, document.body.scrollHeight)"
                )
                page.wait_for_timeout(2000)

        cards = page.query_selector_all("div.base-card")
        print(f"LinkedIn cards found: {len(cards)}")

        for card in cards:
            title_el = card.query_selector("h3")
            company_el = card.query_selector("h4")
            link_el = card.query_selector("a")
            posted_el = card.query_selector(
                "time.job-search-card__listdate, span.job-search-card__listdate"
            )

            if not (title_el and company_el and link_el):
                continue

            jobs.append(Job(
                title=title_el.inner_text().strip(),
                company=company_el.inner_text().strip(),
                link=link_el.get_attribute("href"),
                source="LinkedIn",
                posted=posted_el.inner_text().strip() if posted_el else ""
            ))

        browser.close()

    return jobs
