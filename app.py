# Christopher Storrer's Assessment
from flask import Flask, request, render_template, flash, session, redirect
from rates_and_codes import convert_currency, validate_user_input
# remove later
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)



RESULTS = {}

# List of valid currency codes for form validation
# if code not in valid_currency_codes then raise exception



@app.route("/")
def homepage_form():
    """Shows the homepage with the foreign currency converter form."""
    # Exception that must be removed later, here for debugging only
    #raise
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
   
    #return redirect("/results")
    return render_template("results-page.html",results=RESULTS)

#@app.route("/results")
#def display_results():
#    """Display the results of the currency conversion process"""