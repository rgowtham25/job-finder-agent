# Job Finder Agent

A small Python project that aggregates job postings and fetches job links from sources like LinkedIn and Indeed.

## Features

- Fetch job listings and links from LinkedIn and Indeed (see `fetchers/`)
- Aggregation and filtering of job data
- Simple CLI entry point via `main.py`

## Requirements

- Python 3.10+
- Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script to start fetching and aggregating job postings:

```bash
python main.py
```

## Project Structure

- `fetchers/` - site-specific fetcher modules (`linkedin.py`, `indeed.py`)
- `aggregator.py` - logic to combine results
- `filters.py` - filtering helpers
- `time_utils.py` - time related helpers
- `config.py` - configuration settings
- `models.py` - data models

## Contributing

Open an issue or submit a PR. Please follow existing code style and add tests for new features.

---

If you want, I can also commit this file and push it to the repo. What should I do next?