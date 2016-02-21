import bs4
import cPickle as pickle
import requests

BOTTLESHOP = 'http://www.bellwoodsbrewery.com/product-category/bottleshop/'

PICKLE_FILE = 'beers.pickle'

class Beer(object):

	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.available = True

	def toggle_availability():
		self.available = not self.available

def process(BEERS, available):
	''' '''
	
	previously_available =  [b.title for b in BEERS.values() if b.available]
	for beer in available:
		title = beer['title']
		link = beer['link']
		if title not in BEERS:
			print 'new beer alert: ' + title
			new_beer = Beer(title, link)
			BEERS[title] = new_beer
		else:
			# is it newly available
			if title not in previously_available:
				print 'newly available!'
				BEERS[beer].toggle_availability()
			else:
				print 'still going'
			# is it extinct
	
	currently_available = [b['title'] for b in available]
	for beer in previously_available:
		if beer not in currently_available:
			print 'extinct'
			BEERS[beer].toggle_availability()
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
	process(BEERS, available)

	return

if __name__ == '__main__':
    proc()
