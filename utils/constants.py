# Constants
"""
constants.py

This file contains all configurable constants used across the VivaSim system.
Separating constants from logic improves transparency, maintainability,
and explainability of evaluation rules.
"""

# ------------------------------
# Language Quality Indicators
# ------------------------------

# Words/phrases that indicate uncertainty or low confidence
HEDGING_WORDS = [
    "maybe",
    "i think",
    "i believe",
    "probably",
    "possibly",
    "might be",
    "not sure"
]

# Common filler words that reduce clarity
FILLER_WORDS = [
    "basically",
    "actually",
    "kind of",
    "sort of",
    "like",
    "you know"
]

# ------------------------------
# Structure Evaluation Settings
# ------------------------------

# Indicators used to detect examples in answers
EXAMPLE_INDICATORS = [
    "for example",
    "for instance",
    "such as",
    "consider",
    "example"
]

# ------------------------------
# Scoring Weights
# ------------------------------

# Weight given to keyword relevance in final score
KEYWORD_WEIGHT = 0.6

# Weight given to answer structure in final score
STRUCTURE_WEIGHT = 0.4

# ------------------------------
# Score Limits
# ------------------------------

MAX_SCORE = 100
MIN_SCORE = 0
