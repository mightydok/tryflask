# encoding: utf-8

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Vitaliy'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Bart'},
            'body': 'Party was cool'
        }
    ]
    return render_template('index.html', user=user, posts=posts)
