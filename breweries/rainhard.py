from brewery import Brewery

class Rainhard(Brewery):
	def parse_soup(self):
		soup = self.get_bottleshop_soup()
		parsed_beers = []
		beers = soup.findAll("div", { "data-q_id" : "#portfolio" })
		for b in beers:
			#print b
			title = b.find('strong').getText().split('(')[0]
			if 'COMING SOON' not in title:
				print title
				link = self.bottleshop_url
				parsed_beers.append({'title': title, 'link': link})
		return parsed_beers
