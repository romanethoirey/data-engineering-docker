import unittest
import requests
import os
from sentiment_analysis import score

class FlaskTest(unittest.TestCase):
    def setUp(self):
        os.environ['NO_PROXY'] = '0.0.0.0'
        self.sentence = {
            'positive_sentence': "Im glad to be here",
            'negative_sentence': "Im so sad.",
            'neutral_sentence': "Im a flower."
        }

    def tearDown(self):
        pass

    def test_sentiment_score(self):
        self.assertEqual(score(self.sentence['positive_sentence']), 'Positive')
        self.assertEqual(score(self.sentence['negative_sentence']), 'Negative')
        self.assertEqual(score(self.sentence['neutral_sentence']), 'Neutral')
        
    
    def test_flask_page(self):
        sentence = {
            "sentence": self.sentence['neutral_sentence'],
            'form_type': 'analysis_sentence'
            }

        response = requests.post('http://localhost:5000/', data=sentence)
        self.assertEqual(response.status_code, 200)
        

if __name__ == "__main__":
    unittest.main()