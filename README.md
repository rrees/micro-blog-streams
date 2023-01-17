# micro-blog-streams

Microblogging but deployed on Heroku

Allows you to create small markdown posts with titles but which also allows posts to be organised by their tags to provide streams of related content.

## Running locally

`pipenv run python runserver.py`

Requires an appropriate .env file to supply the application parameters

* DATABASE_URL
* USER_EMAILS
* PASSWORD
* SECRET_KEY