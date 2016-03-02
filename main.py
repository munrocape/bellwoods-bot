from bottle import route, run, static_file
from breweries.bellwoods import Bellwoods
from breweries.burdock import Burdock
from breweries.rainhard import Rainhard
import datetime

CACHE_TIME = 1200

@route('/')
def index():
	return static_file('index.html', root='src/')

@route('/<filename>')
def static(filename):
	return static_file(filename, root='src/')

@route('/css/<filename>')
def css(filename):
	return static_file(filename, 'src/css')

@route('/js/<filename>')
def js(filename):
	return static_file(filename, 'src/js')

@route('/images/<filename>')
def img(filename):
	return static_file(filename, 'src/images')

bellwoods = Bellwoods('Bellwoods', 'http://www.bellwoodsbrewery.com/product-category/bottleshop/')
burdock = Burdock('Burdock', 'http://burdockto.com/bottleshop/')
rainhard = Rainhard('Rainhard', 'http://rainhardbrewing.com/the-bottle-shop/')
breweries = [bellwoods, burdock, rainhard]

last_checked = None
listings = {'beers': []}

def update_listings():
	beers = []
	for b in breweries:
		b.update_listings()
		beers.append(b.get_current_as_json())
	listings['beers'] = beers
	return listings

@route('/api/listings')
def get_listings():
	if last_checked == None:
		global last_checked
		last_checked = datetime.datetime.now()
		print 'populating'
		return update_listings()
	
	now = datetime.datetime.now()
	delta = now - last_checked
	if delta.seconds > CACHE_TIME:
		print 'outdated'
		global last_checked
		last_checked = datetime.datetime.now()
		return update_listings()
	else:
		print 'still fresh'
		return listings

if __name__ == '__main__':
	for b in breweries:
		b.load_listings()
	run(host='0.0.0.0', port=8080)