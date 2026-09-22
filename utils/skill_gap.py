from utils.skill_extractor import extract_skills


HIGH_PRIORITY = {
    "python",
    "java",
    "sql",
    "javascript",
    "machine learning",
    "data structures",
    "algorithms",
    "react",
    "flask",
    "django",
    "spring boot",
    "aws",
    "docker"
}


MEDIUM_PRIORITY = {
    "pandas",
    "numpy",
    "scikit-learn",
    "rest api",
    "git",
    "github",
    "mysql",
    "oracle",
    "mongodb",
    "postgresql",
    "bootstrap",
    "node.js",
    "power bi",
    "tableau"
}


def get_skill_priority(skill):

    if skill in HIGH_PRIORITY:
        return "High"

    if skill in MEDIUM_PRIORITY:
        return "Medium"

    return "Low"


def analyze_skill_gap(resume_text, job_text):

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_text)
    )

    matched_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills - resume_skills
    )

    skill_gap = []

    for skill in missing_skills:

        skill_gap.append({
            "skill": skill,
            "priority": get_skill_priority(skill)
        })

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    skill_gap.sort(
        key=lambda x: priority_order[x["priority"]]
    )

    return {
        "matched": matched_skills,
        "missing": skill_gap
    }