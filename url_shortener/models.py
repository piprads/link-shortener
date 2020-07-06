import string
from datetime import datetime
from random import choices

from .extensions import db 

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(4), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=4))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(128))
    user_agent = db.Column(db.String(512))
    device_type = db.Column(db.String(512))
    geo_lat = db.Column(db.Float)
    geo_long = db.Column(db.Float)
    origin_country = db.Column(db.String(128))
    last_visited = db.Column(db.DateTime)


class UserLinkClicks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('link.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_clicked = db.Column(db.DateTime, default=datetime.now)