import unittest
import requests
import os
from bs4 import BeautifulSoup
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

	def test_positive(self):
		sentence = {
			"sentence": self.sentence['positive_sentence'],
			'form_type': 'analysis_sentence'
			}
		response = requests.post('http://localhost:5000/', data=sentence)
		page = response.content
		soup = BeautifulSoup(page, "html.parser")
		answer = soup.find(id='answer').get_text()
		print(answer)
		self.assertEqual(answer,"The Sentence/Word \"" + self.sentence['positive_sentence'] + "\" is " + 'Positive' + ".")

	def test_neutral(self):
			sentence = {
				"sentence": self.sentence['neutral_sentence'],
				'form_type': 'analysis_sentence'
				}
			response = requests.post('http://localhost:5000/', data=sentence)
			page = response.content
			soup = BeautifulSoup(page, "html.parser")
			answer = soup.find(id='answer').get_text()
			print(answer)
			self.assertEqual(answer,"The Sentence/Word \"" + self.sentence['neutral_sentence'] + "\" is " + 'Neutral' + ".")

	def test_negative(self):
			sentence = {
				"sentence": self.sentence['negative_sentence'],
				'form_type': 'analysis_sentence'
				}
			response = requests.post('http://localhost:5000/', data=sentence)
			page = response.content
			soup = BeautifulSoup(page, "html.parser")
			answer = soup.find(id='answer').get_text()
			print(answer)
			self.assertEqual(answer,"The Sentence/Word \"" + self.sentence['negative_sentence'] + "\" is " + 'Negative' + ".")


	def test_flask_page(self):
		sentence = {
		    "sentence": self.sentence['neutral_sentence'],
		    'form_type': 'analysis_sentence'
		    }
		response = requests.post('http://localhost:5000/', data=sentence)
		self.assertEqual(response.status_code, 200)
    	
    	
if __name__ == "__main__":
    unittest.main()
