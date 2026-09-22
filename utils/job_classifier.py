import joblib
import numpy as np

MODEL_PATH = "models/job_category_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_job_category(text):

    prediction = model.predict([text])[0]

    scores = model.decision_function([text])
    scores = np.asarray(scores).ravel()

    exp_scores = np.exp(scores - np.max(scores))
    probabilities = exp_scores / exp_scores.sum()

    confidence = np.max(probabilities) * 100

    return prediction, round(float(confidence), 2)