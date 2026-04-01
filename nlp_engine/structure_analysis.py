def analyze_structure(answer):

    sentences = [s for s in answer.split(".") if s.strip()]
    length = len(answer.split())

    if len(sentences) >= 4 and length > 40:
        score = 90
    elif len(sentences) >= 3:
        score = 70
    elif len(sentences) >= 2:
        score = 50
    else:
        score = 30

    return {
        "score": score,
        "sentences": len(sentences),
        "length": length
    }