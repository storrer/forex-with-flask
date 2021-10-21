1. Read the assessment requirements
2. complete the conceptual questions
3. ~~Enter start and end times into assessment sheets~~
4. Create directory structure for flask/jinja:

project-dir/
  venv/
  requirements.txt
  app.py
  tests.py
  templates/
      base.html
      form-page.html
      results-page.html
  static
    style.css

# Feature Requirements

1. A form with three inputs:
- One input to type in a three letter currency code to convert from
- One input to type in a three letter currency code to convert to
- One input to type in a number amount to convert
reference image `"form.png"`

2.  Once the form is submitted, make sure that a valid currency code (eg, USD, EUR, JPY) has been input for the currency you are converting from and the currency you are converting to. If the currency code is invalid, you should display a friendly error message to the user letting them know that the currency code is invalid. If the amount is not a valid number, note that, too:

3. If the currency code is valid, you should display a message to the user letting them know the value in the currency they are trying to convert into. When you display the converted currency, it should have an accompanying currency symbol and be rounded to two decimal places. For example, if we were to convert 100 USD to EUR, we would expect a reuslt like “€ 85.16”

4. Refactor your code to move any logic that’s isn’t about the route itself to functions in other Python file(s). Remember, separate your concerns — if you end up with a function that, say, checks if a currency code is valid, you might want this later in a non-Flask app, so move it out of app.py.

# Test Requirements
Write tests for your Flask routes and any other functions you write.

It will take a bit of creative thinking on how to test this — after all, coversion rates between currencies change, so it wouldn’t be a good idea to have a code that makes sure $100 becomes €85.16. Hover below for a hint.

# Clean-up
Uninstall flask_debugtoolbar and autopep8 via pip3