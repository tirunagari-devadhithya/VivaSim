def analyze_structure(answer_text, difficulty="easy"):
    """
    Difficulty-aware structure scoring.
    """

    words = answer_text.strip().split()
    word_count = len(words)

    if difficulty == "easy":
        if word_count >= 15:
            score = 90
        elif word_count >= 8:
            score = 75
        else:
            score = 50

    elif difficulty == "medium":
        if word_count >= 30:
            score = 90
        elif word_count >= 15:
            score = 70
        else:
            score = 40

    else:  # hard
        if word_count >= 50:
            score = 90
        elif word_count >= 25:
            score = 65
        else:
            score = 35

    return {
        "score": score,
        "word_count": word_count
    }