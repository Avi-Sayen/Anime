# Anime
Anime videos directory lister

### Overview
This python script crawls through an anime directory site and generates a text and json file containing links to anime. Basically pirating a pirate
***
###Usage
```shell
main.py
```
Two files are generated one txt and one json
#### Example json
```json
[{"name": "Air Master", "url": "?dir=Anime/Ended/Air Master"},
 {"name": "Air in Summer", "url": "?dir=Anime/Ended/Air in Summer"},
 {"name": "Aishen Qiaokeli-ing", "url": "?dir=Anime/Ended/Aishen Qiaokeli-ing"},
 {"name": "Aiura", "url": "?dir=Anime/Ended/Aiura"},
 {"name": "Akagami no Shirayuki-hime Nandemonai Takaramono, Kono Page", "url": "?dir=Anime/Ended/Akagami no Shirayuki-hime Nandemonai Takaramono, Kono Page"},
 {"name": "Akahori Gedou Hour Rabuge", "url": "?dir=Anime/Ended/Akahori Gedou Hour Rabuge"}]
```
The json contains two values

- Name of the Anime 
- the url

The url doesn't contain the domain name as domain name changes frequently and as such the name can be fetched by sending a "GET" request to-

```html
http://avi-sayen.github.io/Anime
```