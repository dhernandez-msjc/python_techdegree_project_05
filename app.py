import datetime

from flask import (render_template, redirect, url_for, request)
from models import app, db, Project


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/project/<id>')
def detail(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    return render_template('detail.html', projects=projects, project=project)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    projects = Project.query.all()
    project = Project.query.get(id)

    if request.form:
        project.title = request.form['title']
        project.completed = datetime.datetime.strptime(request.form['date'], '%m/%d/%Y')
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github_link = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', projects=projects, project=project)


@app.route('/project/<id>/delete')
def delete(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/project/new', methods=['GET', 'POST'])
def create():
    projects = Project.query.all()
    if request.form:
        new_project = Project(title=request.form['title'],
                              completed=datetime.datetime.strptime(request.form['date'], '%m/%d/%Y'),
                              description=request.form['desc'], skills=request.form['skills'],
                              github_link=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
