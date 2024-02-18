from flask import Flask, render_template
import requests
from utils import bad_return_code

app = Flask(__name__, template_folder='.')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
