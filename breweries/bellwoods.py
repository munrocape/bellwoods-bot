from brewery import Brewery

class Bellwoods(Brewery):
	def parse_soup(self):
		soup = self.get_bottleshop_soup()
		beers = soup.findAll("ul", { "class" : "products" })[0].findAll('li')

		parsed_beers = []

		for beer in beers:
			title = beer.find('h3').getText()
			link = beer.find('a')['href']
			parsed_beers.append({'title': title, 'link': link})

		return parsed_beers