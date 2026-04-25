"""Smoke test using the README usage example (hits live job sites)."""

from __future__ import annotations

import csv

from jobspy import scrape_jobs


def main() -> None:
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "zip_recruiter", "google"],
        search_term="software engineer",
        google_search_term=(
            "software engineer jobs near San Francisco, CA since yesterday"
        ),
        location="San Francisco, CA",
        results_wanted=20,
        hours_old=72,
        country_indeed="USA",
        # linkedin_fetch_description=True
        # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    )
    print(f"Found {len(jobs)} jobs")
    print(jobs.head())
    jobs.to_csv(
        "jobs.csv",
        quoting=csv.QUOTE_NONNUMERIC,
        escapechar="\\",
        index=False,
    )


if __name__ == "__main__":
    main()
