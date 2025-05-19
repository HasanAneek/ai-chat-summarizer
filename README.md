# AI Chat Log Summarizer

A Python tool that analyzes chat logs between users and AI, providing insights and statistics about the conversations.

## Features

- Parses chat logs from .txt files
- Separates messages by speaker (User and AI)
- Counts total messages and messages per speaker
- Extracts most frequent keywords
- Generates comprehensive conversation summaries
- Uses NLTK for advanced text processing
- Supports processing multiple chat logs (bonus feature)

## Requirements

- Python 3.6+
- NLTK library

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-chat-summarizer
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   └── chat_summarizer.py
└── data/
    └── chat.txt
``` 