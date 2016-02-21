import bs4
import cPickle as pickle
import requests

BOTTLESHOP = 'http://www.bellwoodsbrewery.com/product-category/bottleshop/'

PICKLE_FILE = 'beers.pickle'

def process(BEERS, available):
	''' '''
	for beer in available:
		title = beer['title']
		link = beer['link']
		if title not in BEERS:
			print 'new beer alert: ' + title
			BEERS[title] = link
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
