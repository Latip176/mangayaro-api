from src.Latip176.data import WebScrapper
from src.Latip176.reads import ReadComic
from src.Latip176.output import FinalOutput
from flask import Flask, jsonify, request
from flask_cors import CORS
from proxy import proxy as proxies

app = Flask(__name__)
CORS(app)


# --> Route for Search
@app.route("/api/search/")
def search():
    keyword = request.args.get("keyword")
    kategori = request.args.get("category")
    proxy = proxies()
    print(proxy)
    Main = WebScrapper()
    if keyword:
        return Main.route(keyword=keyword)
    else:
        if kategori:
            if kategori == "populer" or kategori == "proyek" or kategori == "terbaru":
                return Main.route(category=kategori)
            else:
                return FinalOutput().results(None, "category is not found!", 400)
    return FinalOutput().results(None, "query is required!", 400)


# --> Route for Get Info and Read
@app.route("/api/reads/")
def information():
    url = request.args.get("url")
    if url:
        url = url.replace("https", "http")
        proxy = proxies()
        print(proxy)
        limit = request.args.get("limit")
        only_chapter = request.args.get("only_chapter")
        Main = ReadComic(url)
        if limit and only_chapter:
            return FinalOutput().results(
                None, "params limit and chapter do not collab!", 400
            )
        else:
            if limit:
                return Main.route(param="limit", limit=limit)
            elif only_chapter:
                return Main.route(param="chapter", only=only_chapter)
            else:
                return Main.route(param="info")

    return FinalOutput().results(None, "url is required!", 400)


# --> Route for Get Image on Single Chapter with url
@app.route("/api/read/")
def read():
    url = request.args.get("url")
    if url:
        url = url.replace("https", "http")
        proxy = proxies()
        print(proxy)
        Main = ReadComic(url)
        return Main.route(param="read", link=url)
    else:
        return FinalOutput().results(None, "url is required"), 400


@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Accept"] = "application/json"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


if __name__ == "__main__":
    app.run()
