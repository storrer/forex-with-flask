#Post Mortem
> "Let's save this man 's life and then have a post-mortem afterwards." - Count Arthur Strong.

Rather than setting a global request dict() on the server, I should use the Flask Session object to communicate with our templates.

While we're doing thatwe should change the render template method in the results view method we should change it to a redirect for a post request to the results page.It is on the results page in that view method that we will call render template.

Something else I'd like to do is some more tests.