from sklearn.metrics import accuracy_score, f1_score, classification_report


def print_basic_metrics(y_true, y_pred):
    print(f"Accuracy = {accuracy_score(y_true, y_pred):.4f}")
    print(f"Macro F1 = {f1_score(y_true, y_pred, average='macro'):.4f}")
    print(f"Weighted F1 = {f1_score(y_true, y_pred, average='weighted'):.4f}")


def get_metrics_dict(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average="macro"),
        "weighted_f1": f1_score(y_true, y_pred, average="weighted"),
    }


def print_classification_report(y_true, y_pred, labels):
    print(classification_report(y_true, y_pred, labels=labels))
