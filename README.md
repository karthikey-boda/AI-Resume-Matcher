# AI Resume Screening & Job Matching System

An AI-powered web application that analyzes resumes against job descriptions, identifies matching and missing skills, predicts job categories, calculates a resume-job compatibility score, and recommends relevant job opportunities.

---

## 🚀 Features

- 📄 PDF resume upload and text extraction
- 🧹 Resume text preprocessing
- 🔍 Automatic skill extraction
- 📊 Resume vs Job Description similarity analysis
- 🎯 Skill matching and skill-gap analysis
- 🤖 Machine Learning based job-category classification
- 📈 Resume-job compatibility scoring
- 💡 Personalized skill recommendations
- 💼 Job recommendations based on resume profile
- 📋 Resume statistics
- 🗄️ Analysis history using SQLite
- 📊 Analysis history analytics
- 🧪 Machine Learning model comparison
- 📉 Confusion matrix visualization
- 📱 Responsive web interface
- 🔗 Job details and application links

---

## 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │        USER         │
                         │      Browser        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Flask Web App   │
                         │       app.py        │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
             ┌────────────┐ ┌─────────────┐ ┌──────────────┐
             │   Resume   │ │    Text     │ │     Job      │
             │   Parser   │ │ Processor   │ │ Description  │
             └─────┬──────┘ └──────┬──────┘ └──────┬───────┘
                   │               │               │
                   └───────────────┼───────────────┘
                                   ▼
                         ┌─────────────────────┐
                         │  Skill Extraction  │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
       ┌──────────────┐      ┌──────────────┐     ┌───────────────┐
       │ TF-IDF Text  │      │ Skill Match  │     │ ML Classifier │
       │  Similarity  │      │   Analysis   │     │   Job Category│
       └──────┬───────┘      └──────┬───────┘     └───────┬───────┘
              │                     │                     │
              └─────────────────────┼─────────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │    Scoring Engine   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Analysis Results  │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
      ┌─────────────┐       ┌──────────────┐       ┌──────────────┐
      │  Skill Gap  │       │     Job      │       │    SQLite    │
      │  Analysis   │       │ Recommender  │       │   Database   │
      └──────┬──────┘       └──────┬───────┘       └──────┬───────┘
             │                     │                      │
             ▼                     ▼                      ▼
      ┌─────────────┐       ┌──────────────┐       ┌──────────────┐
      │   Learning  │       │ Recommended │       │   Analysis   │
      │   Resources │       │     Jobs     │       │   History    │
      └─────────────┘       └──────────────┘       └──────────────┘

🤖 Machine Learning

The system uses Natural Language Processing and Machine Learning techniques to classify job descriptions and resumes into different technology-related job categories.

Job Categories

The current system supports:

Software Developer
Web Developer
Data Analyst
Data Scientist
Machine Learning Engineer
Data Engineer
DevOps Engineer
Cloud Engineer
Cybersecurity Engineer
Database Administrator
Models Evaluated

The training pipeline compares:

Logistic Regression
Linear Support Vector Machine
Multinomial Naive Bayes

The best-performing model is selected based on Weighted F1-score and saved using Joblib.

📊 Model Evaluation

The model evaluation pipeline calculates:

Accuracy
Precision
Recall
Weighted F1-score
Macro F1-score
Confusion Matrix

The evaluation results are stored in:

data/model_results.csv
data/confusion_matrix.csv
Current Model Performance

The current training experiment produced approximately:

Model	Accuracy	Weighted F1	Macro F1
Logistic Regression	85.63%	85.63%	81.36%
Linear SVM	88.37%	88.09%	83.41%
Naive Bayes	59.73%	50.24%	29.20%

The current best-performing model in this experiment is Linear SVM, with approximately 88.37% accuracy and 88.09% weighted F1-score.

Note: These results are based on the project's derived job-category labels. The labels were generated using heuristic rules based on job titles, so the metrics measure agreement with those derived labels rather than independently verified ground-truth categories.

🎯 Resume-Job Matching

The application calculates a compatibility score using three main components:

Final Match Score =
    50% Skill Match
  + 30% Text Similarity
  + 20% Category Match
Skill Match

The system compares the skills extracted from the resume and job description.

It identifies:

Matched skills
Missing skills
Skill match percentage
Text Similarity

The system uses:

TF-IDF
Unigrams
Bigrams
Cosine Similarity

to measure similarity between the resume and job description.

Category Match

The system predicts:

Resume job category
Job description category

and calculates a category compatibility score based on predefined related-category relationships.

The final compatibility score is a project-defined heuristic and should not be interpreted as a standardized ATS score.

💼 Job Recommendation System

The application also recommends relevant job opportunities from the processed job-posting dataset.

The recommendation system considers:

Skill Match
Text Similarity
Category Match
Job Title Relevance

The recommendation score is calculated as:

Job Recommendation Score =
    40% Skill Match
  + 25% Text Similarity
  + 20% Category Match
  + 15% Title Relevance

The system displays the top recommended jobs along with:

Job title
Company
Location
Job category
Match score
Skill match
Text similarity
Category match
Title relevance
Application/view link
🧩 Skill Gap Analysis

The system identifies skills that are required by the job description but missing from the resume.

Missing skills are categorized into:

High Priority
Medium Priority
Low Priority

The application can also provide learning recommendations for supported missing skills.

Example:

Resume Skills:
Python
Java
SQL
Git

Job Requirements:
Python
Java
SQL
Docker
AWS

Matched:
Python
Java
SQL

Missing:
Docker
AWS
📚 Skill Recommendations

The system provides learning recommendations for selected missing skills.

Supported recommendation areas include:

Python
Java
SQL
REST API
Flask
React
JavaScript
Machine Learning
Pandas
NumPy
Scikit-learn
Docker
AWS
Git
📋 Resume Statistics

After analysis, the application displays useful resume statistics such as:

Resume word count
Total detected skills
Number of job-required skills
Matched skills
Missing skills

This helps users understand how closely their resume matches the selected job.

🗄️ Analysis History

The application stores previous resume analyses using SQLite.

Stored information includes:

Resume filename
Match score
Skill match percentage
Matched skills
Missing skills
Job category
Category confidence
Analysis timestamp

The history dashboard also provides:

Total analyses
Average match score
Average skill match
Frequently detected job categories
Frequently missing skills
📊 Model Performance Dashboard

The application includes a dedicated model performance page.

It displays:

Model comparison
Accuracy
Precision
Recall
Weighted F1-score
Macro F1-score
Best-performing model
Confusion matrix

This makes the Machine Learning component easier to evaluate and demonstrate.

🛠️ Technology Stack
Backend
Python
Flask
SQLite
Machine Learning
Scikit-learn
NumPy
TF-IDF
Logistic Regression
Linear SVM
Multinomial Naive Bayes
Joblib
Resume Processing
PyPDF
Frontend
HTML5
CSS3
JavaScript
Chart.js
Development Tools
Git
GitHub
Visual Studio Code
📁 Project Structure
AI-Resume-Matcher/
│
├── app.py
├── train_model.py
├── generate_dataset.py
├── prepare_real_dataset.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── jobs.csv
│   ├── real_jobs.csv
│   ├── model_results.csv
│   ├── confusion_matrix.csv
│   │
│   └── mappings/
│       ├── industries.csv
│       └── skills.csv
│
├── models/
│   └── job_category_model.pkl
│
├── utils/
│   ├── resume_parser.py
│   ├── text_processor.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   ├── skill_matcher.py
│   ├── job_classifier.py
│   ├── skill_recommender.py
│   ├── database.py
│   ├── scoring.py
│   ├── job_recommender.py
│   ├── skill_gap.py
│   └── resume_stats.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   ├── job_details.html
│   └── model_performance.html
│
└── static/
    └── css/
        └── style.css
⚙️ Installation
1. Clone the repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd AI-Resume-Matcher
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000
🧪 Train the Machine Learning Model

To retrain the job-category classification model:

python train_model.py

The training process:

Loads the processed job dataset
Removes duplicate descriptions
Splits the dataset into training and testing sets
Trains multiple classification models
Evaluates each model
Selects the best model based on weighted F1-score
Generates a confusion matrix
Saves the selected model

The trained model is saved as:

models/job_category_model.pkl
📂 Dataset

The project uses job-posting data containing information such as:

Job ID
Company
Job title
Job description
Location
Skills
Experience level
Work type
Salary information
Application information

The processed dataset is used for job-category classification and job recommendations.

The raw dataset is intentionally not included in the repository when it is too large.

🔐 Security and Repository Notes

The following files should not be committed to GitHub:

venv/
.env
*.db
*.sqlite
*.log

Large raw datasets should also be excluded from the repository.

A .gitignore file is included to prevent accidental commits of unnecessary or sensitive files.

⚠️ Limitations

The current version has several limitations:

Skill extraction uses a predefined skill dictionary.
Job-category labels are generated using heuristic title-based rules.
The compatibility score is a project-defined heuristic.
SVM confidence is based on transformed decision scores and is not a calibrated probability.
Job recommendations depend on the available dataset.
Scanned image-only PDF resumes may not provide usable text without OCR.
The current system does not use transformer-based semantic embeddings.
The recommendation system is not intended to represent real-world hiring decisions.
🔮 Future Improvements

Possible future improvements include:

OCR support for scanned resumes
Transformer-based resume embeddings
Sentence-BERT semantic similarity
Larger skill knowledge base
More sophisticated NLP preprocessing
Personalized learning paths
Resume improvement suggestions
Explainable AI for job-category predictions
User authentication
User profiles
Resume version tracking
Docker deployment
Cloud deployment
REST API
Automated testing
Continuous Integration / Continuous Deployment
🎓 Project Purpose

This project was developed as a practical application of:

Python programming
Flask web development
Natural Language Processing
Machine Learning
Information retrieval
Feature extraction
Similarity measurement
Database management
Frontend development

The project demonstrates how multiple software engineering and Machine Learning components can be combined into a single end-to-end application.

👨‍💻 Author

Boda Karthikey

B.Tech – Computer Science and Engineering
CVR College of Engineering

📜 License

This project is developed for educational and portfolio purposes.