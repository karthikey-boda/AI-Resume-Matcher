from utils.job_classifier import predict_job_category

job_description = """
We are looking for a Python Software Developer.
The candidate should have experience with Python, Flask,
REST API, SQL, Git, data structures and algorithms.
The role involves developing backend applications
and working with software development teams.
"""

category, confidence = predict_job_category(job_description)

print("Predicted Category:", category)
print("Confidence:", confidence, "%")