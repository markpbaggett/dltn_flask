from app import app
from flask import render_template, request
from .forms import SearchBox
from .dpla import get_results, print_url, show_results, limit_results


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchBox()
    if request.method == 'POST':
        results = get_results(form.searchtext.data)
        url = print_url(1, form.searchtext.data)
        stuff = show_results(1, form.searchtext.data)
        facets = stuff[1]
        things = stuff[0]
        return render_template('index.html',
                               title='Results',
                               url=url,
                               results=results,
                               things=things,
                               form=form,
                               facets=facets,
                               searchterm=form.searchtext.data)
    return render_template('index.html',
                            title='Home',
                           form=form)

@app.route('/search=<searchterm>&place=<newfacet>')
def results(searchterm, newfacet):
    form = SearchBox()
    results = limit_results(newfacet, searchterm)
    print(results)
    return render_template('index.html',
                           title='Results',
                           things=results,
                           searchterm=searchterm,
                           form=form)