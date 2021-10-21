# conceptual-answers

# What are important differences between Python and JavaScript?
1. I have used JavaScript Only in a client side context. I have only used JavaScript to manipulate data, variables, and the DOM by having a web browser execute the JavaScript code. Python can do, via Flask and Jinja, all the DOM manipulation that JavaScript can; however, with Flask the code is being run on the server and the results, responses with html in the body, or JSON, are sent to the browser for rendering or to some program using my API. 

2. One important difference is that I have not learned how to add event listeners, handlers, to DOM elements with Python. It seems that interaction in that way is JavaScript's job.

# Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you can try to get a missing key (like "c") *without* your programming crashing.

1. Use a `try/catch` block with key access notation `dict["c"]`
2. Use the dict class method `.get("c")`

# What is a unit test?
A unit test is the smallest kind of test. e.g "Does this function return the correct data type? Is this variable holding the correct value?""

# What is an integration test?
Integration Tests are meant to test multiple pieces of software interacting with each other.

# What is the role of web application framework, like Flask?
A web application framework saves time and effort by facilitating the creation of web applications . A framework like flask does this by providing much of the low level code required to get a website or web application working. Frameworks also provide structural guidelines for new projects. Some are more flexible than others.

# You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?
The `/foods/pretzel` choice would be best if this view renders a page that is all about pretzels. However, if the enpoint is something like a generic search results page, the `foods?type=pretzel` key/value choice might be the better fit.

# How do you collect data from a URL placeholder parameter using Flask?
You include the parameter in angle brackets `<>` within the app.route() url string, and you pass the same parameter to the view function.

# How do you collect data from the query string using Flask?
Flask allows the query string to be accessed via the `request.args` property.

# How do you collect data from the body of the request using Flask?
You can access the data in the body with request.get_data() or request.get_json() in the case of a JSON body.

# What is a cookie and what kinds of things are they commonly used for?
A cookie is a small key value pair that are used to give multiple requests a kind of state-ness. The are stored in the browser with variable expiration dates.

# What is the session object in Flask?
> A session makes it possible to remember information from one request to another. The way Flask does this is by using a signed cookie. The user can look at the session contents, but can’t modify it unless they know the secret key.
# What does Flask's `jsonify()` do?
`flask.json.jsonify()` accepts one value, a list, or other data types as arguments. It turns them into a JSON string and returns that JSON object wrapped in a Response.