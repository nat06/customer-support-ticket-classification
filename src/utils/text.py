import re
import pandas as pd


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9.,!?;:'\"()\[\]{}@/\-\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_prediction(pred, queue_list):
    pred = pred.strip().lower()
    normalized = next((q for q in queue_list if q.lower() in pred), "UNKNOWN")
    return normalized
