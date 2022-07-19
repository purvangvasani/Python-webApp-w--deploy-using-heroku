from flask import Flask, render_template, request
from os import getcwd, path

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
