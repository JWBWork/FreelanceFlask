# FreelanceFlask
This repo contains a very tiny API for my freelance site which allows users to contact me via email. The emails themselves are sent using Flask-Mail and SMTP and the API endpoints themselves are built with Flask-RESTful.

Initially I planned on hosting this on AWS using and EC2 instance, but thankfully I discovered AWS elastic beanstalk - which made deployment MUCH easier.

I also wanted to ensure this could easily scale in the future, so from the beginning I built this with flask-blueprints. This way if I ever need to scale this up with multiple API endpoints it would be simple to distribute them across multiple modules and import as a single blueprint.
