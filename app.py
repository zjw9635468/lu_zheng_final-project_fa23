from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import engine
from diabetes import diabetes_result
from heart import heart_result
from kindey import kindey_result

import random
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.String(9), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.Text, nullable=False)

class HealthCondition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    # Add fields based on insurance product selection

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    contract_number = db.Column(db.String(20), unique=True, nullable=False)
    premium = db.Column(db.Float, nullable=False)
    accepted = db.Column(db.Boolean, default=False)

# routes.py
# from flask import render_template

@app.route('/')
def start_page():
    return render_template('start_page.html')

@app.route('/customer_registration', methods=['GET', 'POST'])
def customer_registration():
    if request.method == 'POST':
        ssn = request.form['ssn']
        # Validate and process other form data
        # customer = Customer(ssn=ssn)  # Create a new customer
        # db.session.add(customer)
        # db.session.commit()
        return redirect(url_for('product_selection', ssn = ssn))
    else:
        return render_template('customer_registration.html')

@app.route('/product_selection/<int:ssn>')
def product_selection(ssn):
    return render_template('product_selection.html', user_ssn = ssn)

@app.route('/heart_disease/<int:ssn>', methods=['GET', 'POST'])
def heart_disease(ssn):
    if request.method == 'POST':
        product = 1
        age = request.form['age']
        sex = request.form['sex']
        ChestPainType = request.form['ChestPainType']
        bp = request.form['bp']
        cholesterol = request.form['cholesterol']
        FBSOver120 = request.form['FBSOver120']
        EKGResults = request.form['EKGResults']
        MaxHR = request.form['MaxHR']
        ExerciseAngina = request.form['ExerciseAngina']
        STDepression = request.form['STDepression']
        SlopeOfST = request.form['SlopeOfST']
        NumberOfVesselsFluro = request.form['NumberOfVesselsFluro']
        Thallium = request.form['Thallium']
        
        data = [age, sex, ChestPainType, bp, cholesterol, FBSOver120, EKGResults, MaxHR, ExerciseAngina,
        STDepression, SlopeOfST, NumberOfVesselsFluro, Thallium]

        filename = 'heart_disease_input.csv'
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
        premium = random.randint(4000,6000)
        return redirect(url_for('user_confirmation', ssn = ssn, product = product, premium = premium))
    else:
        return render_template('heart_disease.html', ssn = ssn)

@app.route('/kidney_disease/<int:ssn>', methods=['GET', 'POST'])
def kidney_disease(ssn):
    if request.method == 'POST':
        product = 2
        BloodPressure = request.form['BloodPressure']
        RedBloodCells = request.form['RedBloodCells']
        BloodGlucoseRandom = request.form['BloodGlucoseRandom']
        BloodUrea = request.form['BloodUrea']
        SerumCreatinine = request.form['SerumCreatinine']
        WhiteBloodCellCount = request.form['WhiteBloodCellCount']
        RedBloodCellCount = request.form['RedBloodCellCount']
        Appetite = request.form['Appetite']
        Anemia = request.form['Anemia']
        data = [BloodPressure, RedBloodCells, BloodGlucoseRandom, BloodUrea, SerumCreatinine,
        WhiteBloodCellCount, RedBloodCellCount, Appetite, Anemia]

        filename = 'kidney_disease_input.csv'

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data) 

        premium = random.randint(4000,6000)
        return redirect(url_for('user_confirmation', ssn = ssn, product = product, premium = premium))
    else:
        return render_template('kidney_disease.html', ssn = ssn)
    
@app.route('/diabetes/<int:ssn>', methods=['GET', 'POST'])
def diabetes(ssn):
    if request.method == 'POST':
        product = 3
        Pregnancies = request.form['Pregnancies']
        Glucose = request.form['Glucose']
        BloodPressure = request.form['BloodPressure']
        SkinThickness = request.form['SkinThickness']
        Insulin = request.form['Insulin']
        BMI = request.form['BMI']
        Age = request.form['Age']
        data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Age]

        filename = 'diabetes_input.csv'

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(data)
            
        premium = random.randint(4000,6000)
        return redirect(url_for('user_confirmation', ssn = ssn, product = product, premium = premium))
    else:
        return render_template('diabetes.html', ssn = ssn)

@app.route('/user_confirmation/<int:ssn>/<product>/<premium>')
def user_confirmation(ssn, product, premium):
    if product == 1:
        my_product = "Heart disease insurance"
    elif product == 2:
        my_product = "Chronic disease insurance"
    else:
        my_product = "Diabetes insurance"
    return render_template('user_confirmation.html', ssn = ssn, product = my_product, premium = premium)

@app.route('/payment/<int:ssn>/<premium>')
def payment(ssn, premium):
    return render_template('payment.html', ssn = ssn, premium = premium)

@app.route('/quote_completed/<int:ssn>')
def quote_completed(ssn):
    return render_template('quote_completed.html', ssn = ssn)

if __name__ == '__main__':
    app.run(debug=True)
