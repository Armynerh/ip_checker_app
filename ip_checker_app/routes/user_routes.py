from flask import render_template
from ip_checker_app import app

@app.route('/')
def home():
    return render_template('/index.html')