from flask import Flask, render_template, request
from typograf import make_beautiful


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/action', methods=['POST'])
def beautiful_text():
    text_string = request.form['text']
    beautiful_text_string = make_beautiful(text_string)
    return beautiful_text_string


if __name__ == "__main__":
    app.run()
