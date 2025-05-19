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

## Usage

1. Prepare your chat log file:
   - Create a .txt file in the `data` directory
   - Format messages as "User: message" or "AI: message"
   - Example:
     ```
     User: Hello, I'm interested in learning about Python programming.
     AI: Hello! I'd be happy to help you learn Python.
     ```

2. Run the summarizer:
```bash
python src/chat_summarizer.py
```

3. View the output:
```
Chat Log Summary:
- Total exchanges: 8
- User messages: 4
- AI messages: 4

Most common keywords:
- data: 6 times
- pandas: 5 times
- python: 4 times
- analysis: 3 times
- libraries: 3 times
```

## Testing

Run the test suite to verify all features:
```bash
python -m unittest src/test_chat_summarizer.py -v
```

The test suite verifies:
- Chat log parsing
- Message statistics
- Keyword extraction
- Multiple file processing
- Error handling

## Project Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── chat_summarizer.py    # Main program
│   └── test_chat_summarizer.py  # Test suite
└── data/
    └── chat.txt             # Sample chat log
```

## Features in Detail

1. Chat Log Parsing
   - Reads .txt files with User/AI messages
   - Handles UTF-8 encoding
   - Supports multiple files

2. Message Statistics
   - Counts total messages
   - Separates user and AI messages
   - Provides message distribution

3. Keyword Analysis
   - Uses NLTK for text processing
   - Removes common stopwords
   - Extracts most frequent terms
   - Case-insensitive analysis

4. Error Handling
   - File not found errors
   - Invalid file formats
   - Directory processing errors
   - NLTK download issues

## Contributing

Feel free to submit issues and enhancement requests! 