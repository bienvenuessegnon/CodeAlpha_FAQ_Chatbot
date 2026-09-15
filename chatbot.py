import string

import nltk
import pandas as pd

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# 1. NLTK SETUP
# ============================================================

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")


# ============================================================
# 2. LOAD FAQ DATASET
# ============================================================

DATASET_PATH = "faqs.csv"

try:
    data = pd.read_csv(DATASET_PATH)

except FileNotFoundError:
    print(f"Error: '{DATASET_PATH}' was not found.")
    exit()


# Check required columns
required_columns = {"question", "answer"}

if not required_columns.issubset(data.columns):
    print("Error: The CSV file must contain these columns:")
    print("question,answer")
    exit()


# Remove empty rows
data = data.dropna(subset=["question", "answer"])

questions = data["question"].astype(str).tolist()
answers = data["answer"].astype(str).tolist()


# ============================================================
# 3. TEXT PREPROCESSING
# ============================================================

def preprocess(text):
    """
    Clean and tokenize a text before NLP processing.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Tokenize text
    tokens = word_tokenize(
        text,
        language="english"
    )

    # Remove unnecessary spaces
    tokens = [
        token.strip()
        for token in tokens
        if token.strip()
    ]

    return " ".join(tokens)


# Preprocess all FAQ questions
processed_questions = [
    preprocess(question)
    for question in questions
]


# ============================================================
# 4. TF-IDF VECTORIZATION
# ============================================================

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2)
)

faq_vectors = vectorizer.fit_transform(
    processed_questions
)


# ============================================================
# 5. FIND THE BEST ANSWER
# ============================================================

def get_response(user_question, threshold=0.20):
    """
    Find the FAQ question most similar to the user's question.
    """

    # Preprocess user question
    processed_question = preprocess(
        user_question
    )

    # Convert user question into a TF-IDF vector
    user_vector = vectorizer.transform(
        [processed_question]
    )

    # Calculate cosine similarity
    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )[0]

    # Find the highest similarity score
    best_index = similarities.argmax()
    best_score = similarities[best_index]

    # Check the similarity threshold
    if best_score < threshold:
        return (
            "Sorry, I could not find a relevant answer "
            "to this question in my knowledge base."
        )

    return answers[best_index]


# ============================================================
# 6. CHATBOT INTERFACE
# ============================================================

def start_chatbot():

    print("\n" + "=" * 60)
    print("                 🤖 FAQ AI CHATBOT")
    print("=" * 60)

    print(
        "\nHello! I can answer questions from my knowledge base."
    )
    print("Type 'quit' or 'exit' to leave.\n")

    while True:

        user_question = input("You: ").strip()

        # Handle empty input
        if not user_question:
            print("Bot: Please enter a question.\n")
            continue

        # Exit commands
        if user_question.lower() in {"quit", "exit"}:
            print("Bot: Goodbye! 👋")
            break

        # Generate response
        response = get_response(
            user_question
        )

        print(f"Bot: {response}\n")


# ============================================================
# 7. RUN CHATBOT
# ============================================================

if __name__ == "__main__":
    start_chatbot()