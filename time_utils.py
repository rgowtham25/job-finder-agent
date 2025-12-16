import re

def posted_text_to_days(posted_text: str):
    if not posted_text:
        return None

    text = posted_text.lower()

    if "hour" in text:
        return 0

    if "day" in text:
        n = re.search(r"\d+", text)
        return int(n.group()) if n else None

    if "week" in text:
        n = re.search(r"\d+", text)
        return int(n.group()) * 7 if n else None

    if "month" in text:
        n = re.search(r"\d+", text)
        return int(n.group()) * 30 if n else None

    if "30+" in text:
        return 30

    return None
