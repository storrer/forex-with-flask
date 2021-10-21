# Christopher Storrer's Assessment
from flask import Flask, request, render_template
# Our currency rate getter
from forex_python.converter import CurrencyRates
""" Usage Examples from forex-python.readthedocs.io
        >>> c = CurrencyRates()
        >>> c.get_rates('USD')   # you can directly call get_rates('USD')
        {u'IDR': 13625.0, u'BGN': 1.7433, ...}
        get_rates



"""

# remove later
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)




# List of valid currency codes for form validation
# if code not in valid_currency_codes then raise exception
valid_currency_codes = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD",
                        "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD",
                        "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD",
                        "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK",
                        "BRL", "PLN", "PHP", "ZAR"]


@app.route("/")
def homepage_form():
    """Shows the homepage with the foreign currency converter form."""
    return render_template("form-page.html")

@app.route("/results", methods= ["POST"])
def results_page():
    """"Displays the results of the currency conversion process."""

    return render_template("results-page.html")