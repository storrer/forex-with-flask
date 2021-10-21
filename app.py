# Christopher Storrer's Assessment
from flask import Flask, request, render_template

# remove later
from flask_debugtoolbar import DebugToolbarExtension


# List of valid currency codes for form validation
# if code not in valid_currency_codes then raise exception
valid_currency_codes = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD",
                        "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD",
                        "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD",
                        "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK",
                        "BRL", "PLN", "PHP", "ZAR"]

app = Flask(__name__)

@app.route("/")
def homepage_form():
    """Shows the homepage with the foreign currency converter form."""
    return render_template("form-page.html")

@app.route("/results", methods= ["POST"])
def results_page():
    """"Displays the results of the currency conversion process."""

    return render_template("results-page.html")