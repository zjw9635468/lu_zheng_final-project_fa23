from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
##push test
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
def index():
    return render_template('start_page.html')

@app.route('/customer_registration', methods=['GET', 'POST'])
def customer_registration():
    if request.method == 'POST':
        ssn = request.form['ssn']
        # Validate and process other form data
        customer = Customer(ssn=ssn)  # Create a new customer
        db.session.add(customer)
        db.session.commit()
        return render_template('product_selection.html', customer=customer)
    return render_template('customer_registration.html')

# Similar routes for product_selection, quote_generation, user_confirmation can be added


if __name__ == '__main__':
    app.run(debug=True)
