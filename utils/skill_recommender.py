SKILL_RECOMMENDATIONS = {

    "python": {
        "level": "Beginner → Intermediate",
        "reason": "Useful for backend development, automation, data analysis and machine learning.",
        "resources": [
            "Python fundamentals",
            "Functions and modules",
            "OOP in Python",
            "File handling",
            "Exception handling"
        ]
    },

    "java": {
        "level": "Beginner → Intermediate",
        "reason": "Important for software development and backend engineering.",
        "resources": [
            "Java fundamentals",
            "OOP",
            "Collections Framework",
            "Exception handling",
            "Java Streams"
        ]
    },

    "sql": {
        "level": "Beginner → Intermediate",
        "reason": "Required for working with relational databases and backend applications.",
        "resources": [
            "SELECT queries",
            "WHERE and GROUP BY",
            "JOINs",
            "Subqueries",
            "Indexes"
        ]
    },

    "rest api": {
        "level": "Intermediate",
        "reason": "Important for connecting frontend applications with backend services.",
        "resources": [
            "HTTP methods",
            "REST principles",
            "JSON",
            "GET and POST APIs",
            "API authentication"
        ]
    },

    "flask": {
        "level": "Intermediate",
        "reason": "Useful for building Python web applications and APIs.",
        "resources": [
            "Flask routing",
            "Templates",
            "Forms",
            "REST APIs",
            "Database integration"
        ]
    },

    "react": {
        "level": "Intermediate",
        "reason": "Widely used for building component-based web interfaces.",
        "resources": [
            "Components",
            "Props and state",
            "Hooks",
            "API integration",
            "React Router"
        ]
    },

    "javascript": {
        "level": "Beginner → Intermediate",
        "reason": "Core language for interactive web applications.",
        "resources": [
            "Variables and functions",
            "Arrays and objects",
            "DOM",
            "Events",
            "Async JavaScript"
        ]
    },

    "machine learning": {
        "level": "Intermediate",
        "reason": "Useful for developing predictive and intelligent applications.",
        "resources": [
            "Regression",
            "Classification",
            "Feature engineering",
            "Model evaluation",
            "Scikit-learn"
        ]
    },

    "pandas": {
        "level": "Beginner → Intermediate",
        "reason": "Useful for data manipulation and analysis.",
        "resources": [
            "Series and DataFrames",
            "Filtering",
            "Grouping",
            "Merging",
            "Data cleaning"
        ]
    },

    "numpy": {
        "level": "Beginner",
        "reason": "Provides numerical computing functionality for Python.",
        "resources": [
            "Arrays",
            "Indexing",
            "Array operations",
            "Broadcasting",
            "Linear algebra"
        ]
    },

    "scikit-learn": {
        "level": "Intermediate",
        "reason": "Useful for implementing machine learning algorithms in Python.",
        "resources": [
            "Train/test split",
            "Preprocessing",
            "Classification",
            "Model evaluation",
            "Pipelines"
        ]
    },

    "docker": {
        "level": "Intermediate",
        "reason": "Useful for packaging and deploying applications consistently.",
        "resources": [
            "Images",
            "Containers",
            "Dockerfile",
            "Volumes",
            "Docker Compose"
        ]
    },

    "aws": {
        "level": "Intermediate",
        "reason": "Cloud knowledge is useful for deploying and operating applications.",
        "resources": [
            "EC2",
            "S3",
            "IAM",
            "VPC basics",
            "Cloud deployment"
        ]
    },

    "git": {
        "level": "Beginner",
        "reason": "Essential for source-code version control.",
        "resources": [
            "git init",
            "git add and commit",
            "Branches",
            "Merge",
            "Remote repositories"
        ]
    }
}


def recommend_skills(missing_skills):

    recommendations = []

    for skill in missing_skills:

        skill_lower = skill.lower()

        if skill_lower in SKILL_RECOMMENDATIONS:

            recommendation = SKILL_RECOMMENDATIONS[
                skill_lower
            ].copy()

            recommendation["skill"] = skill

            recommendations.append(
                recommendation
            )

    return recommendations