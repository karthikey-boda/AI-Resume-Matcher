import csv
import random

categories = {
    "Software Developer": [
        "software developer python java sql data structures algorithms object oriented programming",
        "software engineer java python spring boot sql REST API Git",
        "backend developer Java Python SQL API development Git",
        "software development algorithms data structures Java Python database development",
        "application developer Java SQL REST API object oriented programming"
    ],

    "Web Developer": [
        "web developer HTML CSS JavaScript React frontend development",
        "frontend developer HTML CSS JavaScript Bootstrap React",
        "web development JavaScript HTML CSS responsive design React",
        "full stack web developer JavaScript React Node.js HTML CSS",
        "frontend engineer React JavaScript CSS HTML REST API"
    ],

    "Data Analyst": [
        "data analyst SQL Excel Power BI data visualization statistics",
        "business analyst SQL Power BI Excel dashboards data analysis",
        "data analysis Python Pandas SQL visualization statistics",
        "data analyst Excel SQL Tableau Power BI reporting",
        "analyst role SQL Python Pandas data visualization business insights"
    ],

    "Data Scientist": [
        "data scientist Python statistics machine learning Pandas NumPy data analysis",
        "data science Python machine learning statistics predictive modeling",
        "data scientist SQL Python Pandas scikit-learn statistical analysis",
        "machine learning data science Python statistics predictive analytics",
        "data scientist Python NumPy Pandas machine learning visualization"
    ],

    "Machine Learning Engineer": [
        "machine learning engineer Python scikit-learn machine learning model deployment",
        "ML engineer Python TensorFlow PyTorch machine learning model development",
        "machine learning engineer deep learning Python model training deployment",
        "ML developer Python scikit-learn NLP computer vision model optimization",
        "machine learning systems Python TensorFlow model deployment APIs"
    ],

    "Data Engineer": [
        "data engineer Python SQL ETL pipelines data warehouse Apache Spark",
        "data engineering SQL Python ETL pipelines databases Spark",
        "data engineer data pipelines SQL Python cloud data warehouse",
        "ETL developer Python SQL Spark data processing pipelines",
        "data engineering Apache Spark Python SQL databases ETL"
    ],

    "DevOps Engineer": [
        "DevOps engineer Docker Kubernetes Jenkins CI CD Linux Git",
        "DevOps Docker Kubernetes Jenkins AWS Linux automation",
        "DevOps engineer CI CD Docker Kubernetes cloud infrastructure",
        "site reliability engineer Linux Docker Kubernetes monitoring automation",
        "DevOps AWS Jenkins Docker Git Linux deployment automation"
    ],

    "Cloud Engineer": [
        "cloud engineer AWS Azure Docker Kubernetes cloud infrastructure",
        "cloud computing AWS Azure Linux networking infrastructure",
        "cloud engineer AWS EC2 S3 IAM Docker Kubernetes",
        "cloud infrastructure engineer Azure virtual machines networking security",
        "AWS cloud engineer Linux Docker Kubernetes deployment"
    ],

    "Cybersecurity Engineer": [
        "cybersecurity engineer network security vulnerability assessment penetration testing",
        "security engineer Linux network security threat detection SIEM",
        "cybersecurity analyst vulnerability management incident response",
        "information security network security penetration testing risk assessment",
        "security engineer Python Linux threat detection cybersecurity"
    ],

    "Database Administrator": [
        "database administrator SQL Oracle MySQL database backup performance tuning",
        "DBA Oracle SQL Server MySQL database administration",
        "database administrator SQL database security backup recovery",
        "database engineer Oracle MySQL PostgreSQL performance optimization",
        "DBA database monitoring SQL backup recovery performance tuning"
    ]
}

rows = []

for category, descriptions in categories.items():
    for i in range(20):
        description = random.choice(descriptions)

        extra = [
            "team collaboration problem solving",
            "software development lifecycle",
            "version control Git",
            "debugging and testing",
            "technical documentation"
        ]

        selected_extra = random.sample(extra, 2)

        description = description + " " + " ".join(selected_extra)

        rows.append({
            "job_description": description,
            "category": category
        })

random.shuffle(rows)

with open("data/jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["job_description", "category"]
    )

    writer.writeheader()
    writer.writerows(rows)

print("Dataset generated successfully.")
print(f"Total job descriptions: {len(rows)}")
print(f"Categories: {len(categories)}")