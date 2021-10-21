# Here will be the forex_python module imports and currency
# conversion functions.
# Our currency rate getter
from forex_python.converter import CurrencyRates, CurrencyCodes
import decimal

""" Usage Examples from forex-python.readthedocs.io
        >>> c = CurrencyRates()
        >>> c.get_rates('USD')   # you can directly call get_rates('USD')
        {u'IDR': 13625.0, u'BGN': 1.7433, ...}
        get_rates
"""
''' Usage Examples
    Get Currency symbol Using currency code::
    >>> from forex_python.converter import CurrencyCodes
    >>> c = CurrencyCodes()
    >>> c.get_symbol('GBP')
    u'\xa3'
    >>> print c.get_symbol('GBP')
    £
    >>> print c.get_symbol('EUR')
    €
    Get Currency Name using currency code::
    >>> c.get_currency_name('EUR')
    u'European Euro'
    >>> c.get_currency_name('INR')
u'Indian rupee'
'''
def convert_currency(curr_from, curr_to, amount):
    """ Return the value of amount of curr_from in terms of curr_to.
        The return value is a dictionary containing the currency names,
        the currency symbols, and the converted amount.
    """

    # CurrencyRates object for calculating conversions from present rates.
    curr_rates = CurrencyRates()
    # CurrencyCodes object for fetchin
    # g currency names and symbols.
    curr_codes = CurrencyCodes()
    currency_from_name = curr_codes.get_currency_name(curr_from)
    currency_to_name = curr_codes.get_currency_name(curr_to)
    currency_from_symbol = curr_codes.get_symbol(curr_from)
    currency_to_symbol = curr_codes.get_symbol(curr_to)
    value = curr_rates.convert(curr_from, curr_to, decimal.Decimal(amount))
    formatted= '{:.2f}'.format(value)
    results = {"curr_from_name":currency_from_name, 
               "curr_from_symbol":currency_from_symbol, 
               "curr_to_name":currency_to_name,
               "curr_to_symbol":currency_to_symbol,
               "value_in_new_currency": formatted,
               "start_amount": amount}

    return results

def validate_user_input(curr_from, curr_to):
    valid_currency_codes = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD",
                        "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD",
                        "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD",
                        "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK",
                        "BRL", "PLN", "PHP", "ZAR"]
    if curr_from in valid_currency_codes and curr_to in valid_currency_codes:
            return True
    else:
        return False
        