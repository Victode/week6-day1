from . import bp as app 
from flask import render_template, request, redirect, url_for, flash
from app import db
from flask_login import current_user, login_required
from app.blueprints.main.models import  Car

logged_in_user=1
@app.route('/')
@login_required
def home():
    cars = Car.query.all()
    return render_template('home.html',user=current_user, cars=cars)

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/car', methods=['POST'])
@login_required
def create_car():
    car_make = request.form['make']
    car_model = request.form['model']
    car_year = request.form['year']
    car_color = request.form['color']
    car_price = request.form['price']
    # print(car_make,car_model,car_year,car_color,car_price)
    new_car = Car(make=car_make, model=car_model, year=car_year, color=car_color, price=car_price, user_id=1)

    db.session.add(new_car)
    db.session.commit()

    flash('Car added succesfully', 'success')
    return redirect(url_for('main.home'))
