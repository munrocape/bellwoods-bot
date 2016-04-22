from brewery import Brewery

class Burdock(Brewery):
	def parse_soup(self):
		soup = self.get_bottleshop_soup()
		beers = soup.findAll("ul", { "class" : "shop_beer_list" })[0].findAll('li')
		parsed_beers = []
		for beer in beers:
			content = beer.findAll("div", {'class': 'beer_overlay'})
			if content:
				content = content[0]
				title = content.find('h4').getText().split('(')[0]
				in_stock = content.find('p').getText()
				link = self.bottleshop_url
				parsed_beers.append({'title': title, 'link': link, 'stock': in_stock})

		return parsed_beers