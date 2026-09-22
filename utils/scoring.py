def calculate_category_match(resume_category, job_category):
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


def calculate_final_score(
    text_similarity,
    skill_match,
    category_match
):

    final_score = (
        (skill_match * 0.50)
        + (text_similarity * 0.30)
        + (category_match * 0.20)
    )

    return round(final_score, 2)