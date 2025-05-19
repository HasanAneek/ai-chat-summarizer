import unittest
import os
from chat_summarizer import ChatSummarizer

class TestChatSummarizer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.summarizer = ChatSummarizer()
        self.test_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'chat.txt')

    def test_parse_chat_log(self):
        """Test the chat log parsing functionality."""
        user_messages, ai_messages = self.summarizer.parse_chat_log(self.test_file)
        
        # Check if we got the correct number of messages
        self.assertEqual(len(user_messages), 5)  # Based on our sample chat.txt
        self.assertEqual(len(ai_messages), 5)
        
        # Check if the first message is parsed correctly
        self.assertTrue(user_messages[0].startswith("Hello, I'm interested in learning about Python programming"))

    def test_message_statistics(self):
        """Test the message statistics calculation."""
        user_messages, ai_messages = self.summarizer.parse_chat_log(self.test_file)
        stats = self.summarizer.get_message_statistics(user_messages, ai_messages)
        
        # Verify statistics
        self.assertEqual(stats['total_messages'], 10)
        self.assertEqual(stats['user_messages'], 5)
        self.assertEqual(stats['ai_messages'], 5)

    def test_extract_keywords(self):
        """Test the keyword extraction functionality."""
        user_messages, ai_messages = self.summarizer.parse_chat_log(self.test_file)
        keywords = self.summarizer.extract_keywords(user_messages + ai_messages)
        
        # Check if we get the expected number of keywords
        self.assertEqual(len(keywords), 5)
        
        # Check if the keywords are tuples of (word, count)
        for keyword, count in keywords:
            self.assertIsInstance(keyword, str)
            self.assertIsInstance(count, int)
            self.assertGreater(count, 0)

    def test_file_not_found(self):
        """Test handling of non-existent file."""
        user_messages, ai_messages = self.summarizer.parse_chat_log("nonexistent.txt")
        self.assertEqual(user_messages, [])
        self.assertEqual(ai_messages, [])

if __name__ == '__main__':
    unittest.main() 