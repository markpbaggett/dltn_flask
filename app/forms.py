from flask.ext.wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class SearchBox(FlaskForm):
    searchtext = StringField('searchtext')