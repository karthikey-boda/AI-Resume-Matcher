import csv
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = "data/real_jobs.csv"

jobs = []


SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "bootstrap",
    "flask",
    "django",
    "react",
    "node.js",
    "sql",
    "mysql",
    "oracle",
    "mongodb",
    "postgresql",
    "git",
    "github",
    "rest api",
    "data structures",
    "algorithms",
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "power bi",
    "tableau",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "linux",
    "spring boot",
    "jenkins",
    "apache spark",
    "hadoop",
    "etl",
    "cybersecurity",
    "penetration testing",
    "network security"
]


def load_jobs():

    global jobs

    if jobs:
        return jobs

    with open(
        DATA_PATH,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            description = row.get(
                "description",
                ""
            ).strip()

            category = row.get(
                "category",
                ""
            ).strip()

            if description and category:

                jobs.append({
                    "job_id": row.get("job_id", ""),
                    "title": row.get("title", ""),
                    "company_name": row.get(
                        "company_name",
                        ""
                    ),
                    "location": row.get(
                        "location",
                        ""
                    ),
                    "description": description,
                    "category": category,
                    "job_posting_url": row.get(
                        "job_posting_url",
                        ""
                    ),
                    "application_url": row.get(
                        "application_url",
                        ""
                    )
                })

    return jobs


def extract_skills(text):

    text = text.lower()

    detected = set()

    for skill in SKILLS:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill)
            + r"(?!\w)"
        )

        if re.search(pattern, text):

            detected.add(skill)

    return detected


def calculate_skill_similarity(
    resume_text,
    job_text
):

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_text
    )

    if not job_skills:

        return 0.0

    matched = resume_skills.intersection(
        job_skills
    )

    score = (
        len(matched)
        / len(job_skills)
    ) * 100

    return round(score, 2)


def calculate_title_relevance(
    resume_category,
    job_title
):

    title = job_title.lower()

    category_keywords = {

        "Software Developer": [
            "software",
            "developer",
            "engineer",
            "backend",
            "full stack",
            "application"
        ],

        "Web Developer": [
            "web",
            "frontend",
            "front-end",
            "react",
            "ui",
            "developer"
        ],

        "Data Analyst": [
            "data analyst",
            "business analyst",
            "analytics",
            "business intelligence"
        ],

        "Data Scientist": [
            "data scientist",
            "data science"
        ],

        "Machine Learning Engineer": [
            "machine learning",
            "ml engineer",
            "ai engineer",
            "artificial intelligence"
        ],

        "Data Engineer": [
            "data engineer",
            "etl",
            "big data"
        ],

        "DevOps Engineer": [
            "devops",
            "site reliability",
            "sre",
            "release engineer"
        ],

        "Cloud Engineer": [
            "cloud engineer",
            "cloud architect",
            "cloud developer"
        ],

        "Cybersecurity Engineer": [
            "cybersecurity",
            "security engineer",
            "security analyst",
            "information security"
        ],

        "Database Administrator": [
            "database administrator",
            "database engineer",
            "dba"
        ]
    }

    keywords = category_keywords.get(
        resume_category,
        []
    )

    if not keywords:

        return 0.0

    matches = 0

    for keyword in keywords:

        if keyword in title:

            matches += 1

    score = (
        matches
        / len(keywords)
    ) * 100

    return round(
        min(score, 100.0),
        2
    )


def calculate_category_match(
    resume_category,
    job_category
):

    if resume_category == job_category:

        return 100.0

    related_categories = {

        "Software Developer": {
            "Web Developer": 70,
            "Data Engineer": 50,
            "Machine Learning Engineer": 50,
            "DevOps Engineer": 40,
            "Cloud Engineer": 40
        },

        "Web Developer": {
            "Software Developer": 70,
            "Data Engineer": 40,
            "DevOps Engineer": 30
        },

        "Data Analyst": {
            "Data Scientist": 70,
            "Data Engineer": 60,
            "Machine Learning Engineer": 50
        },

        "Data Scientist": {
            "Data Analyst": 70,
            "Machine Learning Engineer": 80,
            "Data Engineer": 60
        },

        "Machine Learning Engineer": {
            "Data Scientist": 80,
            "Software Developer": 50,
            "Data Engineer": 50
        },

        "Data Engineer": {
            "Data Scientist": 60,
            "Data Analyst": 60,
            "Software Developer": 50,
            "Cloud Engineer": 60
        },

        "DevOps Engineer": {
            "Cloud Engineer": 80,
            "Software Developer": 40
        },

        "Cloud Engineer": {
            "DevOps Engineer": 80,
            "Data Engineer": 50,
            "Software Developer": 40
        },

        "Cybersecurity Engineer": {
            "Software Developer": 30
        },

        "Database Administrator": {
            "Data Engineer": 60,
            "Data Analyst": 50
        }
    }

    return related_categories.get(
        resume_category,
        {}
    ).get(
        job_category,
        0.0
    )


def calculate_job_score(
    text_score,
    skill_score,
    category_score,
    title_score
):

    score = (
        (skill_score * 0.40)
        + (text_score * 0.25)
        + (category_score * 0.20)
        + (title_score * 0.15)
    )

    return round(score, 2)


def recommend_jobs(
    resume_text,
    predicted_category,
    top_n=5
):

    all_jobs = load_jobs()

    candidates = []

    for job in all_jobs:

        category_score = calculate_category_match(
            predicted_category,
            job["category"]
        )

        if category_score == 0:

            continue

        candidates.append(job)


    if not candidates:

        return []


    job_texts = [
        job["description"]
        for job in candidates
    ]


    documents = [
        resume_text
    ] + job_texts


    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=20000
    )


    vectors = vectorizer.fit_transform(
        documents
    )


    resume_vector = vectors[0]

    job_vectors = vectors[1:]


    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]


    recommendations = []


    for index, similarity in enumerate(
        similarities
    ):

        job = candidates[index]


        text_score = round(
            float(similarity * 100),
            2
        )


        skill_score = calculate_skill_similarity(
            resume_text,
            job["description"]
        )


        category_score = calculate_category_match(
            predicted_category,
            job["category"]
        )


        title_score = calculate_title_relevance(
            predicted_category,
            job["title"]
        )


        match_score = calculate_job_score(
            text_score,
            skill_score,
            category_score,
            title_score
        )


        recommendations.append({

            "job_id": job["job_id"],

            "title": job["title"],

            "company_name": job[
                "company_name"
            ],

            "location": job[
                "location"
            ],

            "category": job[
                "category"
            ],

            "job_posting_url": job[
                "job_posting_url"
            ],

            "application_url": job[
                "application_url"
            ],

            "text_score": text_score,

            "skill_score": skill_score,

            "category_score": category_score,

            "title_score": title_score,

            "match_score": match_score
        })


    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )


    return recommendations[:top_n]