import bs4
import requests
from abc import ABCMeta, abstractmethod
import datetime
from beer import Beer
import cPickle as pickle

class Brewery(object):

	__metaclass__ = ABCMeta

	def __init__(self, name, bottleshop_url):
		self.name = name
		self.bottleshop_url = bottleshop_url
		self.all_listings = {}
		self.currently_available = {}
		self.fname = 'breweries/listings/' + self.name.lower() + '.pickle'

	def get_bottleshop_soup(self):
		res = requests.get(self.bottleshop_url)
		return bs4.BeautifulSoup(res.text, "html.parser")

	def load_listings(self):
		with open(self.fname, 'r') as f:
			self.all_listings = pickle.load(f)

	def save_listings(self):
		f = open(self.fname, 'w+')
		pickle.dump(self.all_listings, f)

	def update_listings(self):
		available = self.parse_soup()
		self.currently_available = {}
		previously_available = [b.title for b in self.all_listings.values() if b.is_available()]
		for beer in available:
			title = beer['title']
			if title not in self.all_listings:
				# we have a new beer listing
				new_beer = Beer(title, beer['link'])
				self.all_listings[title] = new_beer
			else:
				if title not in previously_available:
					# stocked since last check
					self.all_listings[title].toggle_availability()
			self.currently_available[title] = self.all_listings[title]
		cur_avail = [b['title'] for b in available]
		for title in previously_available:
			if title not in self.currently_available:
				# it has gone out of stock
				print 'soldout'
				self.all_listings[title].toggle_availability()
		self.save_listings()

	def get_current_as_json(self):
		beers = []
		now = datetime.datetime.now()
		for k, v in self.currently_available.iteritems():
			delta = now - v.history[-1]
			recent = delta.days < 1
			beers.append({'name': k, 'link': v.link, 'recently_added': recent})
		return {'brewery': self.name, 'beers': beers}

	@abstractmethod
	def parse_soup():
		''' '''
		pass
