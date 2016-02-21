import bs4
import cPickle as pickle
import requests

BOTTLESHOP = 'http://www.bellwoodsbrewery.com/product-category/bottleshop/'

PICKLE_FILE = 'beerlist.pickle'

def get_current_beers():
    ''' '''

    # request the page
    res = requests.get(BOTTLESHOP)
    # grab the ul that has the products
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # the ul#products has a li for each beer
    beers = soup.findAll("ul", { "class" : "products" })[0].findAll('li')

    parsed_beers = []

    for beer in beers:
    	title = beer.find('h3').getText()
    	link = beer.find('a')['href']
    	parsed_beers.append({'title': title, 'link': link})

    return parsed_beers

def get_beerlist():
	try:
		p = open(PICKLE_FILE, 'r')
		return pickle.load(p)
	except IOError:
		return {}

def save_beerlist():
	p = open(PICKLE_FILE, 'wb')
	pickle.dump(p)
	return

def proc():

	# get the beers

	# process the beers

	return

if __name__ == '__main__':
    proc()
