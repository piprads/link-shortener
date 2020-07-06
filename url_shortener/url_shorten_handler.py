from .models import Link
from .models import User
from .models import UserLinkClicks

class url_shorten_handler:

	def __init__(self):
		pass

	# TBD: Move all business logic to handler
	
	def update_click_stats(url):
		return "Click stats updated"

	def shorten_url(url):
		return "https://skl.sh/2m5UBLg"

	def get_stats(url):
		if url == "https://skl.sh/2m5UBLg" or url == "https://www.skillshare.com":
			return "Times it has been open: 56 \
					Details: \
					- IP 127.0.0.1 - Date: Thu Feb 3rd 2020 \
					- IP 127.0.0.2 - Date: Thu Feb 3rd 2020"
		else:
			return "Times it has been open: 0"
