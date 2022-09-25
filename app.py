from flask import (render_template, url_for, request)
from models import app, db, Project


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/detail')
def detail():
    return render_template('detail.html')


@app.route('/project-form', methods=['GET', 'POST'])
def project_form():
    print(request.form)
    return render_template('projectform.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
