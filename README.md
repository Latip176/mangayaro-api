# mangayaro-api

This project is Web Scraping to mangayaro.net with Python and Made for Rest Api

# updated

- 07 June 2023: readme.md
- 09 June 2023: fix bug, error, readme.md
- 11 June 2023: add fitur reads for get information of comic and image on chapter
# use

## route
### search
```in search you can search comic with params:```
#### search
```
search:
    ?keyword=one piece
```
#### category
```category: populer, proyek, terbaru```
```
category:
    ?category=populer
```
### reads
```in reads you can read a infromation that comic or chapter image```
```
url:
    paste the url of comic mangayaro (required)
    ?url=https://www.mangayaro.net/manga/beyond-myriad-peoples/
    
    limit:
        get omage on chapter with limit
        &limit=10
        
    only_chapter:
        get image on chapter with only chaptrr
        &only_chaptrer=10
    
    limit & only_chapter can't collab!
```

## testing

<a href="https://mangayaro-api-production.up.railway.app/api/search/?category=populer">https://mangayaro-api-production.up.railway.app/api/search/?category=populer</a>
