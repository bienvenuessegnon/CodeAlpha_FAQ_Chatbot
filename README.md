🤖 CodeAlpha — FAQ Chatbot

An NLP-based FAQ chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

The chatbot uses Natural Language Processing (NLP), TF-IDF vectorization, and Cosine Similarity to identify the FAQ that is most relevant to a user's question and return the corresponding answer.

---

📌 Project Overview

The objective of this project is to build a simple FAQ chatbot capable of understanding user questions and finding the most relevant answer from a predefined knowledge base.

Instead of using a large number of hard-coded "if/elif" statements, the system compares the user's question with the available FAQ questions using text similarity techniques.

Main Workflow

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
Best FAQ Match
      ↓
Similarity Threshold
      ↓
Chatbot Response

---

🎯 Objectives

This project implements the main requirements of the CodeAlpha FAQ Chatbot task:

- Collect and organize FAQ questions and answers.
- Preprocess text using NLP techniques.
- Tokenize text using NLTK.
- Convert questions into numerical representations using TF-IDF.
- Calculate Cosine Similarity between the user question and FAQ questions.
- Find the most relevant FAQ.
- Return the corresponding answer.
- Use a similarity threshold to handle unknown questions.
- Provide an interactive chatbot through the terminal.

---

🧠 Technologies Used

Technology| Purpose
Python| Main programming language
NLTK| Text preprocessing and tokenization
Pandas| Loading and manipulating the FAQ dataset
Scikit-learn| TF-IDF and Cosine Similarity
CSV| FAQ dataset storage

---

📂 Project Structure

CodeAlpha_FAQ_Chatbot/
│
├── chatbot.py
├── faqs.csv
├── requirements.txt
└── README.md

"chatbot.py"

Contains the main chatbot implementation:

- Dataset loading
- Text preprocessing
- Tokenization
- TF-IDF vectorization
- Cosine Similarity
- Best-match selection
- Similarity threshold
- User interaction

"faqs.csv"

Contains the FAQ knowledge base.

Example:

question,answer
"What is Python?","Python is a general-purpose programming language."
"What is Artificial Intelligence?","Artificial Intelligence is a field of computer science focused on creating intelligent systems."
"What is Machine Learning?","Machine Learning is a branch of AI that allows systems to learn from data."

"requirements.txt"

Contains the Python packages required to run the project.

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/bienvenuessegnon/CodeAlpha_FAQ_Chatbot.git

2. Navigate to the project directory

cd CodeAlpha_FAQ_Chatbot

3. Install the dependencies

pip install -r requirements.txt

---

📦 Dependencies

The main dependencies are:

pandas
nltk
scikit-learn

They can be installed using:

pip install pandas nltk scikit-learn

---

▶️ Running the Chatbot

Start the chatbot with:

python chatbot.py

The application will run directly in the terminal.

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

1. Dataset Loading

The chatbot loads the FAQ dataset from "faqs.csv".

data = pd.read_csv("faqs.csv")

questions = data["question"].astype(str).tolist()
answers = data["answer"].astype(str).tolist()

This makes it possible to update or expand the knowledge base without modifying the main Python code.

---

2. Text Preprocessing

Before comparing questions, the text is cleaned and normalized.

The preprocessing step includes:

- Converting text to lowercase
- Removing punctuation
- Tokenizing the text
- Removing unnecessary spaces

Example:

"What is Machine Learning?"
             ↓
"what is machine learning"
             ↓
["what", "is", "machine", "learning"]

---

3. TF-IDF Vectorization

The cleaned FAQ questions are transformed into numerical vectors using TF-IDF.

TF-IDF stands for:

Term Frequency — Inverse Document Frequency

It helps represent the importance of words within the FAQ dataset.

The chatbot also uses word pairs (bigrams) to improve matching between related expressions.

---

4. Cosine Similarity

After vectorization, the chatbot calculates the Cosine Similarity between the user's question and every FAQ question.

Conceptually:

User Question
      │
      ├── FAQ 1 → Similarity: 0.12
      ├── FAQ 2 → Similarity: 0.78  ← Best Match
      ├── FAQ 3 → Similarity: 0.21
      └── FAQ 4 → Similarity: 0.05

The FAQ with the highest similarity score is selected.

---

5. Similarity Threshold

The chatbot uses a minimum similarity threshold.

If the best score is too low, the system does not return a potentially incorrect answer.

Example:

User Question
      ↓
Best Similarity = 0.08
      ↓
Below Threshold
      ↓
No Relevant Answer

The chatbot then informs the user that it could not find a relevant answer in its knowledge base.

---

💬 Example Interaction

Known Question

You: Can you explain what machine learning is?

Bot: Machine Learning is a branch of Artificial Intelligence
that allows systems to learn from data.

Similar Question

The chatbot can also handle questions that are not written exactly like the original FAQ.

For example:

You: How does machine learning work?

The system compares the question with the available FAQ questions and selects the closest match based on similarity.

Unknown Question

You: What is the capital of Mars?

Bot: Sorry, I could not find a relevant answer to this
question in my knowledge base.

---

✨ Key Features

- 🤖 NLP-based FAQ chatbot
- 📄 External CSV knowledge base
- 🧹 Text preprocessing
- 🔤 Tokenization
- 📊 TF-IDF vectorization
- 📐 Cosine Similarity
- 🎯 Similarity threshold
- 💬 Interactive terminal interface
- 🔄 Easy-to-expand FAQ dataset
- 🧩 No hard-coded response for every question

---

🚀 Possible Improvements

Future versions could include:

- 🌐 Web-based chatbot interface
- 🧠 Semantic search using sentence embeddings
- 🎯 Intent classification
- 💾 Conversation history
- 🔊 Text-to-Speech
- 🎤 Speech recognition
- 📚 Multiple FAQ categories
- 📈 Automated evaluation metrics
- 🌍 Better multilingual support
- ⚡ More advanced NLP models

---

🎓 CodeAlpha Internship

Program: CodeAlpha Artificial Intelligence Internship

Task: Task 2 — Chatbot for FAQs

This project was developed as part of the CodeAlpha Artificial Intelligence Internship and follows the requirements provided for the FAQ Chatbot task.

---

👨‍💻 Author

Bienvenu Essegnon

Aspiring AI Engineer | Data Science Enthusiast | Full-Stack Developer

GitHub: "@bienvenuessegnon" (https://github.com/bienvenuessegnon)

---

📄 License

This project was developed for educational purposes as part of the CodeAlpha Artificial Intelligence Internship.