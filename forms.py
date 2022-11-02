# forms.py

from wtforms import Form, StringField, SelectField,SubmitField

class GeolocationForm(Form):
    tag_choices =['amenity','building','barrier','boundry','craft','shop']
    tags = SelectField(label='choose tag',choices=tag_choices)
    search_category =StringField('search_category')
    search_input = StringField('search_input')
    