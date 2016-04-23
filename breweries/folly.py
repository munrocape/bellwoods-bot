from brewery import Brewery

class Folly(Brewery):
	def parse_soup(self):
		soup = self.get_bottleshop_soup()
		raw_beers = soup.findAll("div", { "id" : "new-page-section" })[0].findAll("div", {"class": "intrinsic"})
		parsed_beers = []
		for raw_beer in raw_beers:
			link = raw_beer.find("a")['href']
			title = link.split('/')[-1].replace('-', ' ').title()
			parsed_beers.append({'title': title, 'link': link})
		return parsed_beers