# Toronto Bottleshops

This is a website for up-to-date bottleshop listings for breweries in and around Toronto.

Currently, it supports:

- [x] Bellwoods
- [x] Burdock
- [x] Rainhard
- [x] Folly
- [ ] Bloodbrothers
- [ ] Leftfield
- [ ] ???

### Caching, Parsing

The maximum cache lifetime is 1 hour. The cache is stored on-disk as a backup for server restart and is overwritten each time the cache is refreshed.

Each brewery has a parser that is built on top of [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
