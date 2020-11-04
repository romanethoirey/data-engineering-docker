from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

analyser = SentimentIntensityAnalyzer()

def score(sentence):
    if is_pos(sentence):
        print('The sentence is positive.')
        return 'Positive'
    elif is_neg(sentence):
        print('The sentence is negative.')
        return 'Negative'
    elif is_neutral(sentence):
        print('The sentence is neutral.')
        return 'Neutral'

def is_pos(sentence):
    return analyser.polarity_scores(sentence)['compound'] > 0.05

def is_neg(sentence):
    return analyser.polarity_scores(sentence)['compound'] < -0.05

def is_neutral(sentence):
    return not is_pos(sentence) and not is_neg(sentence)

if __name__ == "__main__":
    sentence = input("Write a sentence:\n")
    score(sentence)