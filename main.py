from src.Latip176.data import WebScrapper
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.after_request
def add_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Accept"] = "application/json"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


@app.route("/api/search/")
def search():
    keyword = request.args.get("keyword")
    kategori = request.args.get("category")
    _main = WebScrapper()
    if keyword:
        return _main.route(keyword)
    else:
        if kategori:
            return _main.route(kategori)
    return (
        jsonify(
            {
                "results": [
                    {"data": None, "msg": "query is required!", "status_code": 400}
                ],
                "author": "Latip176",
            },
        ),
        400,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
