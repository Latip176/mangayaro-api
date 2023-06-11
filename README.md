# mangayaro-api

This project is Web Scraping to mangayaro.net with Python and Made for Rest Api

# updated

- 07 June 2023: readme.md
- 09 June 2023: fix bug, error, readme.md

# use

## route
### search
```in search you can search comic with params:```
#### search
```JSON
search:
    ?keyword=one piece
```
#### category
```category: populer, proyek, terbaru```
```
category:
    ?category=populer
```
#### reads
```
url:
    paste the url of comic mangayaro (required)
    ?url=https://www.mangayaro.net/manga/beyond-myriad-peoples/
    
    limit:
        count limit for get image in chapter
        &limit=10
        
    only_chapter:
        only_chapter is for get image in only chapter
        &only_chaptrer=10
```

## testing

<a href="https://mangayaro-api-production.up.railway.app/api/search/?category=populer">https://mangayaro-api-production.up.railway.app/api/search/?category=populer</a>
