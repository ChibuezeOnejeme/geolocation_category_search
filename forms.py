# forms.py

from wtforms import Form, StringField, SelectField,SubmitField

class GeolocationForm(Form):
    search_category =StringField('search_category')
    search_input = StringField('search_input')
    