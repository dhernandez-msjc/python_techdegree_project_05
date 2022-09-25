from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')


@app.route('/project-form')
def project_form():
    return render_template('projectform.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
