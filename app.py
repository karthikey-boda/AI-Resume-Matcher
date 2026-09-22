from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect, secure_filename
import os
from utils.model_evaluation import (
    load_model_results,
    get_best_model,
    load_confusion_matrix
)
from utils.job_recommender import recommend_jobs
from utils.resume_parser import extract_text_from_pdf
from utils.text_processor import clean_text
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_similarity
from utils.skill_matcher import compare_skills
from utils.job_classifier import predict_job_category
from utils.scoring import (
    calculate_final_score,
    calculate_category_match
)
from utils.resume_validator import validate_resume
from utils.skill_gap import analyze_skill_gap
from utils.skill_recommender import recommend_skills
from utils.resume_stats import calculate_resume_stats

from utils.database import (
    create_database,
    save_analysis,
    get_analysis_history,
    get_history_stats,
    clear_analysis_history
)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

create_database()

@app.errorhandler(413)
def file_too_large(error):
    return (
        "File is too large. Please upload a PDF smaller than 5 MB.",
        413
    )
    



@app.route("/model-performance")
def model_performance():

    model_results = load_model_results()

    best_model = get_best_model(
        model_results
    )

    confusion_data = load_confusion_matrix()

    return render_template(
        "model_performance.html",
        model_results=model_results,
        best_model=best_model,
        confusion_data=confusion_data
    )
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/history")
def history():

    analyses = get_analysis_history()

    history_stats = get_history_stats()

    return render_template(
        "history.html",
        analyses=analyses,
        history_stats=history_stats
    )

@app.route("/clear-history", methods=["POST"])
def clear_history():
    clear_analysis_history()
    return redirect("/history")

@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        # Check resume upload

        if "resume" not in request.files:
            return "No resume file uploaded.", 400

        resume_file = request.files["resume"]

        if resume_file is None:
            return "No resume file uploaded.", 400

        if resume_file.filename == "":
            return "Please select a resume PDF.", 400

        if not resume_file.filename.lower().endswith(".pdf"):
            return "Only PDF resume files are supported.", 400

        # Get job description

        job_description = request.form.get(
            "job_description",
            ""
        ).strip()

        if not job_description:
            return "Please enter a job description.", 400

        if len(job_description) < 30:
            return (
                "Please provide a more detailed job description.",
                400
            )

        # Secure filename

        filename = secure_filename(
            resume_file.filename
        )

        # Extract resume text

        resume_text = extract_text_from_pdf(
            resume_file
        )

        if not resume_text or not resume_text.strip():
            return (
                "Could not extract text from this PDF. "
                "Please upload a text-based PDF resume.",
                400
            )

        is_resume, validation_message = validate_resume(resume_text)

        if not is_resume:
            return validation_message, 400
        # Clean text

        cleaned_resume = clean_text(
            resume_text
        )

        cleaned_job = clean_text(
            job_description
        )

        # Extract skills

        resume_skills = extract_skills(
            cleaned_resume
        )

        job_skills = extract_skills(
            cleaned_job
        )

        # Text similarity

        text_similarity = calculate_similarity(
            cleaned_resume,
            cleaned_job
        )

        # Skill comparison

        (
            matched_skills,
            missing_skills,
            skill_match_percentage
        ) = compare_skills(
            resume_skills,
            job_skills
        )

        # Resume category

        (
            resume_category,
            resume_category_confidence
        ) = predict_job_category(
            cleaned_resume
        )

        # Job category

        (
            job_category,
            category_confidence
        ) = predict_job_category(
            cleaned_job
        )

        # Category match

        category_match = calculate_category_match(
            resume_category,
            job_category
        )

        # Final score

        match_score = calculate_final_score(
            text_similarity,
            skill_match_percentage,
            category_match
        )

        # Skill gap

        skill_gap = analyze_skill_gap(
            cleaned_resume,
            cleaned_job
        )

        # Learning recommendations

        recommendations = recommend_skills(
            [
                item["skill"]
                for item in skill_gap["missing"]
            ]
        )

        # Resume statistics

        resume_stats = calculate_resume_stats(
            cleaned_resume,
            resume_skills,
            job_skills,
            matched_skills,
            missing_skills
        )

        # Job recommendations

        job_recommendations = recommend_jobs(
            cleaned_resume,
            resume_category,
            top_n=5
        )

        # Save analysis

        save_analysis(
            filename,
            match_score,
            skill_match_percentage,
            matched_skills,
            missing_skills,
            job_category,
            category_confidence
        )

        # Display result

        return render_template(
            "result.html",

            match_score=match_score,

            text_similarity=text_similarity,

            skill_match_percentage=skill_match_percentage,

            category_match=category_match,

            matched_skills=matched_skills,

            missing_skills=missing_skills,

            resume_skills=resume_skills,

            job_skills=job_skills,

            resume_category=resume_category,

            resume_category_confidence=resume_category_confidence,

            job_category=job_category,

            category_confidence=category_confidence,

            recommendations=recommendations,

            job_recommendations=job_recommendations,

            skill_gap=skill_gap,

            resume_stats=resume_stats
        )

    except Exception as e:

        print("ERROR:", e)

        return (
            "An error occurred while analyzing the resume. "
            "Please check the terminal for details.",
            500
        )
@app.route("/job/<job_id>")
def job_details(job_id):
    from utils.job_recommender import load_jobs

    all_jobs = load_jobs()

    selected_job = None

    for job in all_jobs:
        if job["job_id"] == job_id:
            selected_job = job
            break

    if selected_job is None:
        return "Job not found.", 404

    return render_template(
        "job_details.html",
        job=selected_job
    )

@app.errorhandler(413)
def request_entity_too_large(error):
    return (
        "File is too large. Please upload a PDF smaller than 5 MB.",
        413
    )

if __name__ == "__main__":
    app.run(debug=True)