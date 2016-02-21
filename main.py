import requests
import bs4

BOTTLESHOP = 'http://www.bellwoodsbrewery.com/product-category/bottleshop/'

def get_current_beers():
    ''' '''
    # request the page
    res = requests.get(BOTTLESHOP)
    # grab the ul that has the products
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # a ul has li elements - one for each beer
    beers = soup.findAll("ul", { "class" : "products" })[0].findAll('li')

    for beer in beers:
    	title = beer.find('h3').getText()
    	link = beer.find('a')['href']
    	print title, link

    return

if __name__ == '__main__':
    get_current_beers()
