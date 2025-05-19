import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from typing import Dict, List, Tuple

class ChatSummarizer:
    def __init__(self):
        """Initialize the ChatSummarizer with necessary NLTK downloads."""
        # Download required NLTK data
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def parse_chat_log(self, file_path: str) -> Tuple[List[str], List[str]]:
        """
        Parse the chat log file and separate messages by speaker.
        """
        user_messages = []
        ai_messages = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('User:'):
                        user_messages.append(line[6:].strip())
                    elif line.startswith('AI:'):
                        ai_messages.append(line[4:].strip())
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return [], []
            
        return user_messages, ai_messages

    def get_message_statistics(self, user_messages: List[str], ai_messages: List[str]) -> Dict:
        """
        Calculate basic statistics about the chat.
        """
        return {
            'total_messages': len(user_messages) + len(ai_messages),
            'user_messages': len(user_messages),
            'ai_messages': len(ai_messages)
        }

    def extract_keywords(self, messages: List[str], top_n: int = 5) -> List[Tuple[str, int]]:
        """
        Extract the most frequent keywords from messages.
        """
        # Combine all messages and tokenize
        text = ' '.join(messages).lower()
        tokens = word_tokenize(text)
        
        # Remove stopwords and non-alphabetic tokens
        words = [word for word in tokens if word.isalpha() and word not in self.stop_words]
        
        # Count word frequencies
        word_freq = Counter(words)
        
        return word_freq.most_common(top_n)

def main():
    """Main function to demonstrate the ChatSummarizer functionality."""
    summarizer = ChatSummarizer()
    
    # Example usage
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    chat_file = os.path.join(data_dir, 'chat.txt')
    
    user_messages, ai_messages = summarizer.parse_chat_log(chat_file)
    stats = summarizer.get_message_statistics(user_messages, ai_messages)
    keywords = summarizer.extract_keywords(user_messages + ai_messages)
    
    # Print results
    print("\nChat Log Summary:")
    print(f"- Total exchanges: {stats['total_messages']}")
    print(f"- User messages: {stats['user_messages']}")
    print(f"- AI messages: {stats['ai_messages']}\n")
    
    print("Most common keywords:")
    for word, count in keywords:
        print(f"- {word}: {count} times")

if __name__ == "__main__":
    main() 