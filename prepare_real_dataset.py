import csv
import os


INPUT_PATH = "data/postings.csv"
OUTPUT_PATH = "data/real_jobs.csv"


def classify_job(title):

    title = title.lower()

    if (
        "machine learning" in title
        or "ml engineer" in title
        or "ai engineer" in title
        or "artificial intelligence" in title
    ):
        return "Machine Learning Engineer"

    if "data scientist" in title or "data science" in title:
        return "Data Scientist"

    if (
        "data analyst" in title
        or "business analyst" in title
        or "business intelligence" in title
        or "bi analyst" in title
    ):
        return "Data Analyst"

    if (
        "data engineer" in title
        or "etl developer" in title
        or "big data" in title
    ):
        return "Data Engineer"

    if (
        "devops" in title
        or "site reliability" in title
        or "sre" in title
        or "release engineer" in title
    ):
        return "DevOps Engineer"

    if (
        "cloud engineer" in title
        or "cloud architect" in title
        or "cloud developer" in title
    ):
        return "Cloud Engineer"

    if (
        "cybersecurity" in title
        or "cyber security" in title
        or "information security" in title
        or "security engineer" in title
        or "security analyst" in title
        or "penetration tester" in title
    ):
        return "Cybersecurity Engineer"

    if (
        "database administrator" in title
        or "database engineer" in title
        or "dba" in title
    ):
        return "Database Administrator"

    if (
        "frontend" in title
        or "front-end" in title
        or "web developer" in title
        or "web designer" in title
        or "react developer" in title
        or "ui developer" in title
    ):
        return "Web Developer"

    if (
        "software engineer" in title
        or "software developer" in title
        or "backend developer" in title
        or "back-end developer" in title
        or "java developer" in title
        or "python developer" in title
        or "full stack developer" in title
        or "full-stack developer" in title
        or "application developer" in title
    ):
        return "Software Developer"

    return None


def main():

    os.makedirs("data", exist_ok=True)

    total_rows = 0
    saved_rows = 0
    category_counts = {}

    with open(
        INPUT_PATH,
        "r",
        encoding="utf-8",
        errors="ignore",
        newline=""
    ) as input_file:

        reader = csv.DictReader(input_file)

        fieldnames = [
            "job_id",
            "title",
            "company_name",
            "location",
            "description",
            "category",
            "job_posting_url",
            "application_url"
        ]

        with open(
            OUTPUT_PATH,
            "w",
            encoding="utf-8",
            newline=""
        ) as output_file:

            writer = csv.DictWriter(
                output_file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for row in reader:

                total_rows += 1

                title = (row.get("title") or "").strip()
                description = (row.get("description") or "").strip()

                if not title or not description:
                    continue

                category = classify_job(title)

                if category is None:
                    continue

                writer.writerow({
                    "job_id": row.get("job_id", ""),
                    "title": title,
                    "company_name": row.get("company_name", ""),
                    "location": row.get("location", ""),
                    "description": description,
                    "category": category,
                    "job_posting_url": row.get("job_posting_url", ""),
                    "application_url": row.get("application_url", "")
                })

                saved_rows += 1
                category_counts[category] = (
                    category_counts.get(category, 0) + 1
                )

    print("Dataset preparation complete.")
    print(f"Total rows processed: {total_rows}")
    print(f"Rows saved: {saved_rows}")

    print("\nCategory distribution:")

    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()