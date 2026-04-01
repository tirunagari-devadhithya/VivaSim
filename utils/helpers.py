# Helper functions
"""
helpers.py

This module contains small utility functions that are reused
across different parts of the VivaSim system.
These functions do not perform evaluation or scoring.
"""

import re


def normalize_text(text):
    """
    Normalizes text by:
    - Lowercasing
    - Removing extra whitespace

    Used before lightweight text checks.
    """

    if text is None:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def count_phrase_occurrences(text, phrase_list):
    """
    Counts how many times phrases from a given list
    appear in the text.

    Parameters:
    - text: input string
    - phrase_list: list of phrases to check

    Returns:
    - count (integer)
    """

    if not text:
        return 0

    normalized_text = normalize_text(text)
    count = 0

    for phrase in phrase_list:
        if phrase in normalized_text:
            count += normalized_text.count(phrase)

    return count


def safe_percentage(part, whole):
    """
    Safely calculates percentage without division errors.

    Returns:
    - integer percentage
    """

    if whole == 0:
        return 0

    return int((part / whole) * 100)
