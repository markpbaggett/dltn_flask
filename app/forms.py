from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchBox(Form):
    searchtext = StringField('searchtext')