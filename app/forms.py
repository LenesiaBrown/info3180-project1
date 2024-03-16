from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, SelectField
from wtforms.validators import InputRequired


class AddPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])     
    description = TextAreaField('Description', validators=[InputRequired()])
    bedroom = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathroom = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    ptype = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    location = StringField('Location', validators=[InputRequired()]) 
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only Image Files!')])    