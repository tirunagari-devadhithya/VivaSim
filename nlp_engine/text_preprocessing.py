# Text preprocessing
import spacy
import string

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Preprocesses the input text for NLP analysis.

    Steps:
    1. Lowercasing
    2. Tokenization using spaCy
    3. Stopword removal
    4. Punctuation removal
    5. Lemmatization

    Returns a list of clean tokens.
    """

    if text is None or len(text.strip()) == 0:
        return []

    # Convert text to lowercase
    text = text.lower()

    # Process text using spaCy
    doc = nlp(text)

    clean_tokens = []

    for token in doc:
        # Skip stopwords
        if token.is_stop:
            continue

        # Skip punctuation
        if token.text in string.punctuation:
            continue

        # Skip spaces
        if token.is_space:
            continue

        # Append lemmatized form
        clean_tokens.append(token.lemma_)

    return clean_tokens
