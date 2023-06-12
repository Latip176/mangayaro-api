# mangayaro-api

This project is Web Scraping to mangayaro.net with Python and Made for Rest Api

# updated

- 07 June 2023: readme.md
- 09 June 2023: fix bug, error, readme.md
<<<<<<< HEAD
- 11 June 2023: add fitur reads for get information of comic and get image on chapter
# use

## route
### search
```in search you can search comic with params:```
#### keyword
```keyword: title of comic u can find```
```
/search/
search:
    ?keyword=one piece
```
#### category
```category: populer, proyek, terbaru```
```
/search/
category:
    ?category=populer
```
### reads
```in reads you can read a infromation that comic or get image on chapter```
```
/reads/
url:
    paste the url of comic mangayaro (required). example:
    ?url=https://www.mangayaro.net/manga/beyond-myriad-peoples/
    
    limit:
        get image on chapter with limit. example:
        ?url=test&limit=10
        
    only_chapter:
        get image on chapter with only chapter. example:
        ?url=test&only_chaptrer=10
    
    limit & only_chapter can't collab!
```
## testing example
### search category
```
https://mangayaro-api-production.up.railway.app/api/search/?category=populer
```
### reads information comic
```
https://mangayaro-api-production.up.railway.app/api/reads/?url=https://www.mangayaro.net/manga/beyond-myriad-peoples/
```
### reads image on chapter with limit
```
https://mangayaro-api-production.up.railway.app/api/reads/?url=https://www.mangayaro.net/manga/beyond-myriad-peoples&limit=5
```
### reads image on chapter with only_chapter
```
https://mangayaro-api-production.up.railway.app/api/reads/?url=https://www.mangayaro.net/manga/beyond-myriad-peoples&only_chapter=3
```
