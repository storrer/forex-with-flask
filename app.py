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
