
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

`$cd /url_shortener`
>>> from url_shortener import create_app
>>> from url_shortener.extensions import 
>>> from url_shortener.models import Link
>>> from url_shortener.models import User
>>> from url_shortener.models import UserLinkClicks
>>> db.create_all(app=create_app())`

### Accessing the db

`$ sqlite3 url_shortener/db.sqlite3`

![alt text](https://github.com/piprads/link-shortener/blob/master/url_shortener/img/Screen%20Shot%202020-07-05%20at%2011.34.55%20PM.png?raw=true)

### Running the service and urls

#### start the flask server
#### `$ flask run`

![alt_text](https://github.com/piprads/link-shortener/blob/master/url_shortener/img/Screen%20Shot%202020-07-05%20at%2011.38.29%20PM.png?raw=true)

#### `http://127.0.0.1:5000/`

![alt_text](https://github.com/piprads/link-shortener/blob/master/url_shortener/img/Screen%20Shot%202020-07-05%20at%2011.38.54%20PM.png?raw=true)

#### `http://127.0.0.1:5000/f5hc`

#### `http://127.0.0.1:5000/stats`

![alt_text](https://github.com/piprads/link-shortener/blob/master/url_shortener/img/Screen%20Shot%202020-07-05%20at%205.41.13%20PM.png?raw=true)

### Running the app via CLI

`python click shorten "http://www.skillshare.com"`
`python click stats "http://127.0.0.1:5000/f5hc"`

## Follow-ups

