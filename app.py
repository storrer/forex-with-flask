# Christopher Storrer's Assessment
from flask import Flask, request, render_template, flash, session, redirect
from rates_and_codes import convert_currency, validate_user_input

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"



# global results variable, should be a session variable, not sure how to implement this
RESULTS = {}




@app.route("/")
def homepage_form():
    """Shows the homepage with the foreign currency converter form."""
   
    return render_template("form-page.html")

@app.route("/calculate", methods= ["POST"])
def evaluate_currency():
    """Calclulate the results using rates_and_codes.py"""
    # curr_from, curr_to, amount
    from_currency = request.form['curr_from']
    to_currency = request.form['curr_to']
    if validate_user_input(from_currency, to_currency):
        flash("Converting your chosen currencies: ")
    else:
        flash("Please use a valid currrency code.")
        return render_template("form-page.html")
    amount = request.form['amount']
    RESULTS = convert_currency(from_currency, to_currency, amount)
   
    return render_template("results-page.html",results=RESULTS)

