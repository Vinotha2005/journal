# logic/phase_splitter.py

import re

def split_sentences(text):
    """
    Splits journaling text into meaningful sentences.
    Handles '.', '?', '!' safely.
    """

    if not text or not isinstance(text, str):
        return []

    # Split by sentence-ending punctuation
    parts = re.split(r'[.!?]+', text)

    # Clean and return non-empty sentences
    sentences = [p.strip() for p in parts if p.strip()]
    return sentences
