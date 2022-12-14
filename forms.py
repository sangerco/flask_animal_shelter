from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

default_img = 'https://image.shutterstock.com/image-vector/dog-cat-pet-shop-vector-260nw-1743739268.jpg'

class AddPetForm(FlaskForm):
    """ Form for adding snacks """

    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot by blank")])
    species = StringField("Pet Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message="Species must be a cat, a dog, or a porcupine!")])
    photo_url = StringField("Photo URL (if available)", validators=[Optional(), URL()], default=default_img)
    age = IntegerField("Pet Age (if known", validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30!")])
    notes = StringField("Notes")
    available = BooleanField("Availability")