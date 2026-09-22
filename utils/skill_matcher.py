def compare_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(resume_set.intersection(job_set))
    missing_skills = sorted(job_set - resume_set)

    if len(job_set) == 0:
        skill_match_percentage = 0.0
    else:
        skill_match_percentage = (
            len(matched_skills) / len(job_set)
        ) * 100

    return (
        matched_skills,
        missing_skills,
        round(skill_match_percentage, 2)
    )