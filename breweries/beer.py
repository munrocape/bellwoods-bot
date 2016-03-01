import datetime

class Beer(object):

	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.available = False
		self.history = []
		self.toggle_availability()

	def toggle_availability(self):
		t = datetime.datetime.now()
		self.history.append(t)
	
	def is_available(self):
		return len(self.history) % 2 == 1