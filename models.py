from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key='True')
    title = db.Column('Title', db.String())
    completed = db.Column('Completed', db.DateTime)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    github_link = db.Column('GitHub', db.Text)

    def __repr__(self):
        return f'''<Project (Title: {self.title})
                Completed: {self.completed}
                Description: {self.description}
                Skills: {self.skills}
                GitHub Link: {self.github_link}>'''
