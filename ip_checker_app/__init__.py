from flask import Flask

app = Flask(__name__, instance_relative_config=True)
# app.config.from_pyfile('config.py')

from ip_checker_app.routes import user_routes  # Import routes after app initialization
