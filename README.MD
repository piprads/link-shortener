
# Link Shortener

A service for link shortening that accepts a web URL and returns a shortened URL that
resolves to the original URL.

This is a flask app which shortens a full url to a 4 char url and saves counts for each time someone visits the urls. The functionality can be accessed via flask routes or via click CLI.

### Assumptions

* Auth is out of scope for the app
* Redirect implementation is out of scope
* links / user / clicks are the entities in the db; For simplicity of MVP, SQLite database is used and 
* columns for metadata are are mentioned in the models.py but assumed they can be stored from request object
* a very high level MVC have been followed; there are a number of TBDs in the current state of the app due to time constraint
* No tests have been implemented


## Current Status

The service can:
* Shorten a full url to a 4 char (ascii+digits) string
* Fetch a full url from a shorten url
* Save count visit for a short_url
* Persist short_url, full_url, visits for urls
* Model supports user and metadata attributes (currently unused)
* CLI (fully hardcoded) using `click` to support shorten and stats commands
* Working templates for /add_link (shorten), /stats (url stats)


## How to Use

### Setting up the app

### Setting up the DB

path: /url_shortener
>>> from url_shortener import create_app
>>> from url_shortener.extensions import 
>>> from url_shortener.models import Link
>>> db.create_all(app=create_app())

### Running the app via templates

### Running the app via CLI

## Follow-ups
