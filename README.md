🤖 CodeAlpha — FAQ Chatbot

📌 Project Overview

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.

The goal of this project is to build an FAQ chatbot capable of automatically finding the most relevant answer to a user's question.

Instead of relying on a large number of hard-coded "if/elif" conditions, the chatbot uses Natural Language Processing (NLP) techniques to compare the user's question with a predefined FAQ dataset.

The system uses TF-IDF vectorization and Cosine Similarity to identify the most similar question and return its corresponding answer.

---

🎯 Objectives

The project implements the main requirements of CodeAlpha's FAQ Chatbot task:

- Collect and organize frequently asked questions and answers.
- Preprocess text using NLP techniques.
- Tokenize user questions and FAQ questions.
- Convert text into numerical representations using TF-IDF.
- Compare questions using Cosine Similarity.
- Identify the most similar FAQ.
- Return the corresponding answer.
- Use a similarity threshold to handle unknown questions.
- Provide an interactive chatbot through the terminal.

---

🧠 Technologies Used

- Python
- NLTK — Natural Language Processing and tokenization
- Pandas — Dataset loading and manipulation
- Scikit-learn — TF-IDF vectorization and Cosine Similarity
- CSV — FAQ dataset storage

---

📂 Project Structure

CodeAlpha_FAQ_Chatbot/
│
├── chatbot.py
├── faqs.csv
├── requirements.txt
└── README.md

"chatbot.py"

Contains the main chatbot logic:

1. Load the FAQ dataset.
2. Preprocess the questions.
3. Tokenize the text.
4. Create TF-IDF vectors.
5. Calculate Cosine Similarity.
6. Find the best matching FAQ.
7. Check the similarity threshold.
8. Return the appropriate response.
9. Handle user interaction through the terminal.

"faqs.csv"

Contains the questions and answers used by the chatbot.

Example:

question,reponse
"What is Python?","Python is a general-purpose programming language..."
"What is Machine Learning?","Machine Learning is a branch of Artificial Intelligence..."

"requirements.txt"

Contains the Python dependencies required to run the project.

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/CodeAlpha_FAQ_Chatbot.git

2. Navigate to the project directory

cd CodeAlpha_FAQ_Chatbot

3. Install the dependencies

pip install -r requirements.txt

---

📦 Dependencies

The project uses the following main libraries:

pandas
nltk
scikit-learn

---

▶️ Running the Chatbot

Run the following command:

python chatbot.py

The chatbot will start directly in the terminal.

Example:

============================================================
                 🤖 FAQ AI CHATBOT
============================================================

Hello! I can answer questions from my knowledge base.
Type 'quit' or 'exit' to leave.

You: What is machine learning?

Bot: Machine Learning is a branch of Artificial Intelligence
that allows systems to learn from data.

To exit the chatbot:

You: quit

Bot: Goodbye! 👋

---

🔍 How It Works

The chatbot follows a simple NLP pipeline:

User Question
      ↓
Text Preprocessing
      ↓
Tokenization
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Most Similar FAQ
      ↓
Similarity Threshold
      ↓
Return Answer

1. Text Preprocessing

The chatbot prepares the text before comparison by:

- converting text to lowercase;
- removing punctuation;
- tokenizing the sentence;
- removing unnecessary spaces.

2. TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical vectors.

It gives higher importance to words that are more informative for distinguishing between different questions.

3. Cosine Similarity

Cosine Similarity measures how similar two text vectors are.

The chatbot compares the user's question against all questions in the FAQ dataset and selects the one with the highest similarity score.

4. Similarity Threshold

A minimum similarity threshold is used to avoid returning an unrelated answer.

If the best similarity score is below the threshold, the chatbot informs the user that it does not have a relevant answer.

---

💡 Example

Known Question

You: Can you explain what machine learning is?

The chatbot searches the FAQ dataset for the most similar question and returns the corresponding answer.

Unknown Question

You: What is the capital of Mars?

If no FAQ is sufficiently similar, the chatbot responds:

Bot: Sorry, I could not find a relevant answer to this
question in my knowledge base.

---

📊 Key Features

- ✅ FAQ dataset stored separately from the source code
- ✅ Natural Language Processing
- ✅ Text preprocessing
- ✅ Tokenization
- ✅ TF-IDF vectorization
- ✅ Cosine Similarity
- ✅ Similarity threshold
- ✅ Interactive terminal chatbot
- ✅ Easy-to-expand FAQ database

---

🚀 Possible Improvements

Future versions could include:

- A graphical or web-based interface.
- Semantic search using sentence embeddings.
- Intent classification.
- Better handling of synonyms and paraphrases.
- Conversation history.
- Multiple FAQ categories.
- Voice input and text-to-speech.
- Automated evaluation of chatbot accuracy.

---

🎓 CodeAlpha Internship

Program: CodeAlpha Artificial Intelligence Internship

Task: Task 2 — Chatbot for FAQs

This project was developed to fulfill the requirements of the FAQ Chatbot task provided by CodeAlpha.

---

👨‍💻 Author

Bienvenu Essegnon

Aspiring AI Engineer | Data Science Enthusiast | Full-Stack Developer

---

📄 License

This project was developed for educational purposes as part of the CodeAlpha Artificial Intelligence Internship.