import re


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


def extract_skills(text):
    text = text.lower()

    detected_skills = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            detected_skills.append(skill)

    return sorted(detected_skills)