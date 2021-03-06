from flask import Flask, request, render_template
from sentiment_analysis import score

app = Flask(__name__)

def classify_sentence(sentence):
    content = "The Sentence/Word \"{}\" is {}.".format(sentence, score(sentence))
    return render_template('index.html',
                            content=content)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        if details['form_type'] == 'analysis_sentence':
            return classify_sentence(details['sentence'])
    return render_template('index.html', content='')

if __name__ == '__main__':
    app.run(host='0.0.0.0')