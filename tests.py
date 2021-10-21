# Tests for forex converstion functions
from app import app
from rates_and_codes import validate_user_input, convert_currency
from unittest import TestCase

class ConvertCurrencyTestCase(TestCase):
    def test_convert_currency(self):
        self.assertDictContainsSubset({'value_in_new_currency': '1.00'},convert_currency('EUR','EUR', '1.00'))