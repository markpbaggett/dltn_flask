from app import app
from flask import render_template, request
from .forms import LoginForm
from .dpla import get_results, print_url, show_results

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        results = get_results(form.searchtext.data)
        url = print_url(1, form.searchtext.data)
        things = show_results(1, form.searchtext.data)
        return render_template('index.html',
                               title='Results',
                               url=url,
                               results=results,
                               things=things,
                               form=form)
    return render_template('index.html',
                            title='Home',
                           form=form)
