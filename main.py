import bs4
import cPickle as pickle
import requests
import datetime

BOTTLESHOP = 'http://www.bellwoodsbrewery.com/product-category/bottleshop/'

PICKLE_FILE = 'beers.pickle'

SOLD_OUT = 0
RESTOCK = 1
INSTOCK = 2
NEW = 3

class Beer(object):

	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.available = False
		self.history = []
		self.toggle_availability()

	def toggle_availability():
		t = datetime.datetime.now()
		self.history.append(t)
		self.available = not self.available

def log(state, beer):
	if state == SOLD_OUT:
		print 'sold out: ' + beer.title
	elif state == RESTOCK:
		print 'restock: ' + beer.title
	elif state == INSTOCK:
		print 'still going: ' + beer.title
	elif state == NEW:
		print 'new: ' + beer.title
	else:
		print 'invalid state'

def process_current_availability(BEERS, available):
	''' '''
	
	previously_available =  [b.title for b in BEERS.values() if b.available]
	for beer in available:
		title = beer['title']
		link = beer['link']
		if title not in BEERS:
			new_beer = Beer(title, link)
			log(NEW, new_beer)
			BEERS[title] = new_beer
		else:
			# is it newly available
			if title not in previously_available:
				BEERS[beer].toggle_availability()
				log(RESTOCK, BEERS[title])
			else:
				log(INSTOCK, BEERS[title])
	
	currently_available = [b['title'] for b in available]
	for title in previously_available:
		if title not in currently_available:
			BEERS[title].toggle_availability()
			log(SOLD_OUT, BEERS[title])
	save_beer_list(BEERS)

def get_current_beers():
    '''Pings the website and returns a list of [name, link] for each currently available beer'''

    # request the page
    res = requests.get(BOTTLESHOP)
    # grab the ul that has the products
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # the ul.products has a li for each beer
    beers = soup.findAll("ul", { "class" : "products" })[0].findAll('li')

    parsed_beers = []

    for beer in beers:
    	title = beer.find('h3').getText()
    	link = beer.find('a')['href']
    	parsed_beers.append({'title': title, 'link': link})

    return parsed_beers

def get_beer_list():
	'''Attempts to load a pickle file that corresponds to historical beer info.
	Returns an empty dictionary if the file does not exist.'''

	try:
		p = open(PICKLE_FILE, 'r')
		return pickle.load(p)
	except IOError:
		return {}

def save_beer_list(BEERS):
	''' '''
	
	p = open(PICKLE_FILE, 'wb')
	pickle.dump(BEERS, p)
	return

def proc():
	''' '''

	BEERS = get_beer_list()

	# get the beers
	available = get_current_beers()
	# process the beers
	process_current_availability(BEERS, available)

	return

if __name__ == '__main__':
    proc()
