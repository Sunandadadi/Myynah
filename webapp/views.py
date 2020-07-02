from flask import render_template
from webapp.models.partners import Partners
from webapp.models.Utils import Utils
from configuration.default import Settings
from webapp import app


@app.route('/')
def index():
    return render_template("index.html", Settings=Settings)

@app.route('/search_partners/<search_query>')
def search_partners(search_query):
    obj = Partners(search_query)
    response = obj.query_all_partners()
    return render_template("results_page.html", response=response, Settings=Settings)

@app.route('/about')
def about():
    about = Utils.fetch_about_content()
    return render_template("about.html", about=about, Settings=Settings)
