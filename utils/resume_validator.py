import re


RESUME_SECTIONS = [
    "education",
    "experience",
    "work experience",
    "professional experience",
    "skills",
    "technical skills",
    "projects",
    "certifications",
    "achievements",
    "summary",
    "objective",
    "profile",
    "internship",
    "internships",
    "employment",
    "qualifications",
]


RESUME_KEYWORDS = [
    "resume",
    "curriculum vitae",
    "cv",
    "developer",
    "engineer",
    "programming",
    "software",
    "python",
    "java",
    "javascript",
    "sql",
    "html",
    "css",
    "github",
    "linkedin",
]


def validate_resume(text):
    if not text or not text.strip():
        return False, "The PDF does not contain readable text."

    text_lower = text.lower()

    word_count = len(text_lower.split())

    if word_count < 80:
        return False, (
            "This document does not contain enough text to be recognized "
            "as a resume."
        )

    section_matches = 0

    for section in RESUME_SECTIONS:
        pattern = r"\b" + re.escape(section) + r"\b"

        if re.search(pattern, text_lower):
            section_matches += 1

    keyword_matches = 0

    for keyword in RESUME_KEYWORDS:
        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, text_lower):
            keyword_matches += 1

    email_found = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )
    )

    phone_found = bool(
        re.search(
            r"(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)",
            text
        )
    )

    resume_indicators = 0

    if section_matches >= 2:
        resume_indicators += 2
    elif section_matches == 1:
        resume_indicators += 1

    if keyword_matches >= 3:
        resume_indicators += 2
    elif keyword_matches >= 1:
        resume_indicators += 1

    if email_found:
        resume_indicators += 1

    if phone_found:
        resume_indicators += 1

    if resume_indicators < 3:
        return False, (
            "The uploaded PDF does not appear to be a resume. "
            "Please upload a valid resume containing sections such as "
            "Education, Skills, Experience, or Projects."
        )

    return True, "Resume validated successfully."