def calculate_resume_stats(
    resume_text,
    resume_skills,
    job_skills,
    matched_skills,
    missing_skills
):
    word_count = len(resume_text.split())

    return {
        "word_count": word_count,
        "total_skills": len(resume_skills),
        "job_skills": len(job_skills),
        "matched_skills": len(matched_skills),
        "missing_skills": len(missing_skills)
    }