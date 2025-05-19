import unittest
import os
import tempfile
import shutil
from chat_summarizer import ChatSummarizer

class TestChatSummarizer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.summarizer = ChatSummarizer()
        self.test_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'chat.txt')
        
        # Create a temporary directory for multiple file tests
        self.temp_dir = tempfile.mkdtemp()
        self.create_test_files()

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        shutil.rmtree(self.temp_dir)

    def create_test_files(self):
        """Create test files in the temporary directory."""
        # Create first test file
        with open(os.path.join(self.temp_dir, 'chat1.txt'), 'w') as f:
            f.write("User: Hello\nAI: Hi\nUser: How are you?\nAI: I'm good")
        
        # Create second test file
        with open(os.path.join(self.temp_dir, 'chat2.txt'), 'w') as f:
            f.write("User: What's Python?\nAI: Python is a programming language\nUser: Thanks\nAI: You're welcome")

    def test_parse_chat_log(self):
        """Test the chat log parsing functionality."""
        user_messages, ai_messages = self.summarizer.parse_chat_log(self.test_file)
        
        # Check if we got the correct number of messages
        self.assertEqual(len(user_messages), 4)  # Based on our sample chat.txt
        self.assertEqual(len(ai_messages), 4)
        
        # Check if the first message is parsed correctly
        self.assertTrue(user_messages[0].startswith("Hello, I'm interested in learning about Python programming"))

    def test_message_statistics(self):
        """Test the message statistics calculation."""
        user_messages, ai_messages = self.summarizer.parse_chat_log(self.test_file)
        stats = self.summarizer.get_message_statistics(user_messages, ai_messages)
        
        # Verify statistics
        self.assertEqual(stats['total_messages'], 8)
        self.assertEqual(stats['user_messages'], 4)
        self.assertEqual(stats['ai_messages'], 4)

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

    def test_process_multiple_files(self):
        """Test processing multiple chat log files."""
        results = self.summarizer.process_multiple_files(self.temp_dir)
        
        # Check if we got results for both files
        self.assertEqual(len(results), 2)
        self.assertIn('chat1.txt', results)
        self.assertIn('chat2.txt', results)
        
        # Check statistics for first file
        chat1_stats = results['chat1.txt']['statistics']
        self.assertEqual(chat1_stats['total_messages'], 4)
        self.assertEqual(chat1_stats['user_messages'], 2)
        self.assertEqual(chat1_stats['ai_messages'], 2)
        
        # Check statistics for second file
        chat2_stats = results['chat2.txt']['statistics']
        self.assertEqual(chat2_stats['total_messages'], 4)
        self.assertEqual(chat2_stats['user_messages'], 2)
        self.assertEqual(chat2_stats['ai_messages'], 2)

    def test_process_empty_directory(self):
        """Test processing an empty directory."""
        empty_dir = tempfile.mkdtemp()
        try:
            results = self.summarizer.process_multiple_files(empty_dir)
            self.assertEqual(results, {})
        finally:
            shutil.rmtree(empty_dir)

    def test_process_invalid_directory(self):
        """Test processing a non-existent directory."""
        results = self.summarizer.process_multiple_files("nonexistent_dir")
        self.assertEqual(results, {})

if __name__ == '__main__':
    unittest.main() 