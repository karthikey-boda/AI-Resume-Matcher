import sqlite3
from collections import Counter

DATABASE = "resume_matcher.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_filename TEXT,
            match_score REAL,
            skill_match_percentage REAL,
            matched_skills TEXT,
            missing_skills TEXT,
            job_category TEXT,
            category_confidence REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(
    resume_filename,
    match_score,
    skill_match_percentage,
    matched_skills,
    missing_skills,
    job_category,
    category_confidence
):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses (
            resume_filename,
            match_score,
            skill_match_percentage,
            matched_skills,
            missing_skills,
            job_category,
            category_confidence
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        resume_filename,
        match_score,
        skill_match_percentage,
        ", ".join(matched_skills),
        ", ".join(missing_skills),
        job_category,
        category_confidence
    ))

    connection.commit()
    connection.close()


def get_analysis_history():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM analyses
        ORDER BY created_at DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history


def get_history_stats():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM analyses
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    total = len(rows)

    if total == 0:
        return {
            "total": 0,
            "average_match_score": 0,
            "average_skill_match": 0,
            "top_categories": [],
            "top_missing_skills": []
        }

    average_match_score = round(
        sum(float(row["match_score"] or 0) for row in rows) / total,
        2
    )

    average_skill_match = round(
        sum(float(row["skill_match_percentage"] or 0) for row in rows) / total,
        2
    )

    categories = Counter()

    for row in rows:
        category = row["job_category"] or "Unknown"
        categories[category] += 1

    missing_skills = Counter()

    for row in rows:
        skills = row["missing_skills"] or ""

        for skill in skills.split(","):
            skill = skill.strip()

            if skill:
                missing_skills[skill] += 1

    return {
        "total": total,
        "average_match_score": average_match_score,
        "average_skill_match": average_skill_match,
        "top_categories": categories.most_common(5),
        "top_missing_skills": missing_skills.most_common(5)
    }


def clear_analysis_history():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM analyses")

    connection.commit()
    connection.close()