from flask import Flask, render_template, request
#from requests import get
#from json import dump
from os import getcwd, path
#from os import mkdir
#from tqdm import tqdm
#from bs4 import BeautifulSoup
#from multiprocessing import Pool, Process
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form['nm']
        print(url)
        print(getcwd())
        print(path.exists('/service'))
    else:
        user = request.args.get('nm')
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
