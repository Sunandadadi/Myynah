from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config.from_object('configuration')

import webapp.views

# app.config.from_object('configuration.default')
# app.config.from_envvar('APP_CONFIG_FILE')

# @app.errorhandler(404)
# def not_found(error):
    # return "Oops! We coouldn't find the page you are looking for"
    # return render_template('404.html'), 404
