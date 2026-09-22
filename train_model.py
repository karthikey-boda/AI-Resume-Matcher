import csv
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


DATASET_PATH = "data/real_jobs.csv"
MODEL_PATH = "models/job_category_model.pkl"
RESULTS_PATH = "data/model_results.csv"
CONFUSION_MATRIX_PATH = "data/confusion_matrix.csv"


def load_dataset():

    texts = []
    labels = []

    with open(DATASET_PATH, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            text = row.get("description", "").strip()
            label = row.get("category", "").strip()

            if text and label:

                texts.append(text)
                labels.append(label)

    return texts, labels


def remove_duplicates(texts, labels):

    seen = set()

    clean_texts = []
    clean_labels = []

    for text, label in zip(texts, labels):

        key = text.lower().strip()

        if key not in seen:

            seen.add(key)

            clean_texts.append(text)
            clean_labels.append(label)

    return clean_texts, clean_labels


def create_models():

    models = {

        "Logistic Regression": Pipeline([
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=2,
                    max_df=0.95
                )
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000
                )
            )
        ]),

        "Linear SVM": Pipeline([
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=2,
                    max_df=0.95
                )
            ),
            (
                "classifier",
                LinearSVC()
            )
        ]),

        "Naive Bayes": Pipeline([
            (
                "tfidf",
                TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2),
                    min_df=2,
                    max_df=0.95
                )
            ),
            (
                "classifier",
                MultinomialNB()
            )
        ])
    }

    return models


def evaluate_model(model, X_train, X_test, y_train, y_test):

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    macro_f1 = f1_score(
        y_test,
        predictions,
        average="macro",
        zero_division=0
    )

    return {
        "model": model,
        "predictions": predictions,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "macro_f1": macro_f1
    }


def save_results(results):

    os.makedirs(
        os.path.dirname(RESULTS_PATH),
        exist_ok=True
    )

    with open(
        RESULTS_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "Weighted F1",
            "Macro F1"
        ])

        for result in results:

            writer.writerow([
                result["name"],
                round(result["accuracy"] * 100, 2),
                round(result["precision"] * 100, 2),
                round(result["recall"] * 100, 2),
                round(result["f1"] * 100, 2),
                round(result["macro_f1"] * 100, 2)
            ])


def main():

    print("\nLoading dataset...")

    texts, labels = load_dataset()

    print("Dataset size:", len(texts))

    texts, labels = remove_duplicates(
        texts,
        labels
    )

    print(
        "Dataset after cleaning:",
        len(texts)
    )

    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.20,
        random_state=42,
        stratify=labels
    )

    print(
        "\nTraining samples:",
        len(X_train)
    )

    print(
        "Testing samples:",
        len(X_test)
    )

    models = create_models()

    results = []

    best_model = None
    best_name = None
    best_f1 = 0

    for name, model in models.items():

        print("\n" + "=" * 60)

        print(name)

        print("=" * 60)

        result = evaluate_model(
            model,
            X_train,
            X_test,
            y_train,
            y_test
        )

        result["name"] = name

        results.append(result)

        print(
            "Accuracy:",
            round(result["accuracy"], 4)
        )

        print(
            "Precision:",
            round(result["precision"], 4)
        )

        print(
            "Recall:",
            round(result["recall"], 4)
        )

        print(
            "Weighted F1:",
            round(result["f1"], 4)
        )

        print(
            "Macro F1:",
            round(result["macro_f1"], 4)
        )

        if result["f1"] > best_f1:

            best_f1 = result["f1"]

            best_model = result["model"]

            best_name = name


    print("\n" + "=" * 60)

    print("MODEL COMPARISON")

    print("=" * 60)

    for result in results:

        print(
            f'{result["name"]}: '
            f'Accuracy={result["accuracy"]:.4f}, '
            f'Weighted F1={result["f1"]:.4f}, '
            f'Macro F1={result["macro_f1"]:.4f}'
        )


    print("\nBest Model:")

    print(best_name)

    print(
        "Weighted F1:",
        round(best_f1, 4)
    )


    best_result = None

    for result in results:

        if result["name"] == best_name:

            best_result = result

            break


    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            best_result["predictions"],
            zero_division=0
        )
    )


    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            best_result["predictions"]
        )
    )

    save_confusion_matrix(
    y_test,
    best_result["predictions"]
    )


    save_results(results)


    os.makedirs(
        os.path.dirname(MODEL_PATH),
        exist_ok=True
    )

    joblib.dump(
        best_model,
        MODEL_PATH
    )

    print("\nModel saved to:")

    print(MODEL_PATH)

    print("\nModel comparison saved to:")

print(RESULTS_PATH)

print("\nConfusion matrix saved to:")

print(CONFUSION_MATRIX_PATH)

def save_confusion_matrix(y_test, predictions):

    labels = sorted(set(y_test))

    matrix = confusion_matrix(
        y_test,
        predictions,
        labels=labels
    )

    with open(
        CONFUSION_MATRIX_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Actual / Predicted"] + labels
        )

        for label, row in zip(labels, matrix):

            writer.writerow(
                [label] + row.tolist()
            )

if __name__ == "__main__":

    main()