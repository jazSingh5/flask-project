from flask import render_template, url_for, flash, redirect
from City.forms import TopCities
from City import app

top_cities = [
    "Paris", "London", "Rome", "Tahiti"
]


title = 'Top Cities'

name = 'Your Name'  # change this to your name


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = TopCities()
    if form.validate_on_submit():
        flash(f'Form Submitted for {form.city_name.data}!',
              category='success')
        return redirect(url_for('home'))

    return render_template("home.html",
                           title=title,
                           name=name,
                           top_cities=top_cities,
                           form=form)