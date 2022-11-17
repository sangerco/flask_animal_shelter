from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "doggo"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """ list pets, show pics, display availability """
    pets = Pet.query.all()
    return render_template('home-page.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_page():
    """ show pet add form, handle incoming data """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {name} the {species} to the database.")
        return redirect("/add")
    else:
        return render_template('add.html', form=form)

@app.route('/pets/<int:id>')
def show_pet_page(id):
    """ render view of each pet in shelter
        add edit and return buttons"""

    pet = Pet.query.get_or_404(id)
    return render_template('/view-pet.html', pet=pet)

@app.route('/pets/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet_page(id):
    """ show edit pet page, handle incoming data """

    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/view-pet.html', pet=pet)
    else:
        return render_template('edit-pet.html', form=form)