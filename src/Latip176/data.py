from src.Latip176.module import *


# --> Class Response
class Response(object):
    def __init__(self, session=requests.Session(), dict={}):
        self.__session = session  # --> self session: untuk menyimpan requests Session
        self.__data_dict = dict  # --> self data dict: untuk menampung data dictinory

    # --> Request ke web
    def __response(self, query=None) -> str:
        if query == None:
            return self._Response__session.get(
                "https://www.mangayaro.net/", headers={"UserAgent": "Chrome"}
            )
        else:
            return self._Response__session.get(
                f"https://www.mangayaro.net/?s={query}", headers={"UserAgent": "Chrome"}
            )

    # --> Final Output
    def __setup(self, data_list: list, query: str) -> dict:
        priv_list = []
        if query == "populer":
            for data in data_list:
                url, title, chapter, rating = data
                priv_list.append(
                    {"url": url, "title": title, "chapter": chapter, "rating": rating}
                )
        elif query == "terbaru" or query == "proyek":
            for data in data_list:
                url, bg_url, title, update = data
                priv_list.append(
                    {"url": url, "bg_url": bg_url, "title": title, "update": update}
                )
        else:
            for data in data_list:
                url, bg_url, title, chapter, rating, tipe = data
                priv_list.append(
                    {
                        "url": url,
                        "bg_url": bg_url,
                        "title": title,
                        "chapter": chapter,
                        "rating": rating,
                        "tipe_komik": tipe,
                    }
                )
        self._Response__data_dict.update(
            {
                "results": [
                    {
                        "data": priv_list,
                        "msg": "Success",
                        "status_code": 200,
                        "jumlah_data": len(priv_list),
                    }
                ],
                "author": "Latip176",
            }
        )
        return json.dumps(self._Response__data_dict), 200


# --> Class Turunan dari Class Response
class WebScrapper(Response):
    def __init__(self, list=[], dict={}):
        super().__init__()
        self.__data_list = list  # --> self data list: untuk menampung data list

    def route(self, query: str = None) -> dict:
        if query:
            if query == "populer" or query == "terbaru" or query == "proyek":
                soup = BeautifulSoup(
                    self._Response__response().text, "html.parser"
                )  # --> BeautifulSoup
                if query == "populer":  # --> Jika Query memasukan "populer"
                    populer = self.populer_hari_ini(
                        soup
                    )  # --> Menuju ke Function populer_hari_ini
                    return self._Response__setup(populer, query)
                elif query == "proyek":  # --> Jika Query memasukan "proyek"
                    proyek = self.pembaruan_projek(
                        soup
                    )  # --> Menuju ke Function pembaruan_projek
                    return self._Response__setup(proyek, query)
                elif query == "terbaru":
                    terbaru = self.pembaruan_terbaru(
                        soup
                    )  # --> Menuju ke Function pembaruan_terbaru
                    return self._Response__setup(terbaru, query)
            else:
                soup = BeautifulSoup(
                    self._Response__response(query).text, "html.parser"
                )  # --> BeautifulSoup
                search = self.searchComic(soup)
                return self._Response__setup(search, query)
        else:
            return {
                "results": [
                    {"data": None, "msg": "query is required!", "status_code": 400}
                ],
                "author": "Latip176",
            }, 400

    def populer_hari_ini(
        self, soup
    ) -> list:  # --> Function untuk Scraping data komik Populer Hari Ini
        content = (
            soup.find("div", attrs={"id": "content"})
            .find("div", attrs={"class": "listupd"})
            .findAll("div", attrs={"class": "bs"})
        )  # --> Find div yang berisikan data populer sesuai yang ada di websitenya
        for i in content:
            link = i.find("a", href=True)
            bigor = link.find("div", attrs={"class": "bigor"})
            data_list = (url, title, chapter, rating) = [
                link.get("href"),
                " ".join(
                    re.findall(
                        "([a-zA-Z0-9]+)",
                        str(bigor.find("div", attrs={"class": "tt"}).string),
                    )
                ),
                re.findall(
                    "\d+", str(bigor.find("div", attrs={"class": "epxs"}).string)
                )[0],
                bigor.find("div", attrs={"class": "numscore"}).string,
            ]  # --> Scraping mengambil data: url, judul, jumlah chapter, rating. komik
            self._WebScrapper__data_list.append(
                data_list
            )  # --> Menambahkan data hasil Scraping ke Self data list
        return self._WebScrapper__data_list  # --> mengembalikan nilai Self data list

    def pembaruan_projek(
        self, soup
    ) -> list:  # --> Function untuk Scraping data komik Pembaruan Projek
        content = (
            soup.find("div", attrs={"id": "content"})
            .find("div", attrs={"class": "postbody"})
            .findAll("div", attrs={"class": "bixbox"})[0]
            .findAll("div", attrs={"class": "utao"})
        )  # --> Find div yang berisikan data populer sesuai yang ada di websitenya
        for i in content:
            imgu, luf = i.find("div", attrs={"class": "imgu"}).find(
                "a", href=True
            ), i.find("div", attrs={"class": "luf"})

            data_list = (url, bg_url, title, update) = [
                imgu.get("href"),
                imgu.find("img").get("src"),
                " ".join(
                    re.findall(
                        "([a-zA-Z0-9]+)",
                        str(imgu.get("title")),
                    )
                ),
                [
                    {
                        str(i + 1): {
                            "chapter": x.find("a").string,
                            "time": x.find("span").string,
                        }
                        for i, x in enumerate(luf.find("ul").findAll("li"))
                    }
                ],
            ]
            self._WebScrapper__data_list.append(
                data_list
            )  # --> Menambahkan data hasil Scraping ke Self data list
        return self._WebScrapper__data_list  # --> mengembalikan nilai Self data list

    def pembaruan_terbaru(
        self, soup
    ) -> list:  # --> Function untuk Scraping data komik Pembaruan Projek
        content = (
            soup.find("div", attrs={"id": "content"})
            .find("div", attrs={"class": "postbody"})
            .findAll("div", attrs={"class": "bixbox"})[1]
            .findAll("div", attrs={"class": "utao"})
        )  # --> Find div yang berisikan data populer sesuai yang ada di websitenya
        for i in content:
            imgu, luf = i.find("div", attrs={"class": "imgu"}).find(
                "a", href=True
            ), i.find("div", attrs={"class": "luf"})

            data_list = (url, bg_url, title, update) = [
                imgu.get("href"),
                imgu.find("img").get("src"),
                " ".join(
                    re.findall(
                        "([a-zA-Z0-9]+)",
                        str(imgu.get("title")),
                    )
                ),
                [
                    {
                        str(i + 1): {
                            "chapter": x.find("a").string,
                            "time": x.find("span").string,
                        }
                        for i, x in enumerate(luf.find("ul").findAll("li"))
                    }
                ],
            ]
            self._WebScrapper__data_list.append(
                data_list
            )  # --> Menambahkan data hasil Scraping ke Self data list
        return self._WebScrapper__data_list  # --> mengembalikan nilai Self data list

    def searchComic(
        self, soup=None
    ):  # --> Function untuk Scraping data komik searching
        content = (
            soup.find("div", attrs={"id": "content"})
            .find("div", attrs={"class": "listupd"})
            .findAll("div", attrs={"class": "bs"})
        )
        pagination = soup.find("div", attrs={"class": "pagination"})
        page = pagination.find("a", attrs={"class": "next page-numbers"})
        for x in content:
            bigor, limit = x.find("div", attrs={"class": "bigor"}), x.find(
                "div", attrs={"class": "limit"}
            )
            href = x.find("a", href=True)
            data_list = (url, bg_url, title, chapter, rating, tipe) = [
                href.get("href"),
                limit.find("img", attrs={"src": True}).get("src"),
                " ".join(
                    re.findall(
                        "([a-zA-Z0-9]+)",
                        str(href.get("title")),
                    )
                ),
                bigor.find("div", attrs={"class": "epxs"}).string,
                bigor.find("div", attrs={"class": "numscore"}).string,
                "Warna"
                if limit.find("span", attrs={"class": "colored"})
                else "Tidak Berwarna",
            ]
            self._WebScrapper__data_list.append(
                data_list
            )  # --> Menambahkan data hasil Scraping ke Self data list
        if page:
            self.searchComic(
                BeautifulSoup(requests.get(page.get("href")).text, "html.parser")
            )  # --> Menambahkan data hasil Scraping ke Self data list
        return self._WebScrapper__data_list  # --> mengembalikan nilai Self data list
