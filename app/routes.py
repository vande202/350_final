from flask import Flask,render_template, url_for
from app import app

@app.route('/')
def test():

    return render_template('index.html', swear='BITches and assholes')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error=None


    return render_template('index.html', swear='BITches and assholes')
