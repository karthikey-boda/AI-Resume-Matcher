import csv

RESULTS_PATH = "data/model_results.csv"


def load_model_results():

    results = []

    try:

        with open(
            RESULTS_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                results.append({
                    "model": row["Model"],
                    "accuracy": float(row["Accuracy"]),
                    "precision": float(row["Precision"]),
                    "recall": float(row["Recall"]),
                    "weighted_f1": float(row["Weighted F1"]),
                    "macro_f1": float(row["Macro F1"])
                })

    except FileNotFoundError:

        return []

    return results


def get_best_model(results):

    if not results:
        return None

    return max(
        results,
        key=lambda x: x["weighted_f1"]
    )


def load_confusion_matrix():

    matrix = []

    try:

        with open(
            "data/confusion_matrix.csv",
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            rows = list(reader)

            if not rows:
                return {
                    "labels": [],
                    "matrix": []
                }

            labels = rows[0][1:]

            for row in rows[1:]:

                matrix.append(
                    [int(value) for value in row[1:]]
                )

            return {
                "labels": labels,
                "matrix": matrix
            }

    except FileNotFoundError:

        return {
            "labels": [],
            "matrix": []
        }