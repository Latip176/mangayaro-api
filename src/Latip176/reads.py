from src.Latip176.module import *
from src.Latip176.output import FinalOutput


class Main(object):
    def __init__(self, session=None, url: str = None):
        self.__session = session
        self.__url = url

    def __Response(self, query=None) -> str:
        if query == "info":
            return BeautifulSoup(
                self._Main__session.get(self._Main__url).text, "html.parser"
            )
        else:
            return BeautifulSoup(self._Main__session.get(query).text, "html.parser")


class ReadComic(Main):
    def __init__(self, url: str = None):
        super().__init__(requests.Session(), url)
        self.__data_list = []  # --> data: for list information comic
        self.__data_chapter = []  # --> data: for list data chapter founded
        self.__data_img = []  # --> data: for all image panel on chapter comic

    def route(
        self, limit=None, param=None, only=None, link=None
    ) -> dict:  # --> function route url and condition
        self._ReadComic__data_chapter.clear()
        self._ReadComic__data_img.clear()
        if param == "read":
            regex = re.findall(".*?chapter\-(\d+).*?", str(link))[0]
            soup = self._Main__Response(link)
            preaderarea = re.findall(
                'src="(.*?)"',
                str(soup.find("div", {"id": "readerarea"})),
            )
            self._ReadComic__data_img.append({f"Chapter {regex}": preaderarea})
            return FinalOutput().results(self._ReadComic__data_img, "Success", 200)
        info = self.getInfo()  # --> get information
        __information = FinalOutput().results(info, "success", 200)
        if param == "info":
            return __information
        elif param == "chapter" or param == "limit":
            if param == "chapter":
                information = info[0]
                if int(only) <= information["chapter_count"]:
                    infos = information["chapter_content"][int(only) - 1]
                    soup = self._Main__Response(infos["url"])
                    preaderarea = re.findall(
                        'src="(.*?)"',
                        str(soup.find("div", {"id": "readerarea"})),
                    )
                    self._ReadComic__data_img.append(
                        {f"{infos['chapter']}": preaderarea}
                    )
                else:
                    return FinalOutput().results(
                        None,
                        f"the number of limits entered is too much! count: {information['chapter_count']} Chapter only",
                        400,
                    )
            elif param == "limit":
                information = info[0]
                if int(limit) <= information["chapter_count"]:
                    for x, y in enumerate(information["chapter_content"]):
                        if x == int(limit):
                            break
                        soup = self._Main__Response(y["url"])
                        preaderarea = re.findall(
                            'src="(.*?)"',
                            str(soup.find("div", {"id": "readerarea"})),
                        )
                        self._ReadComic__data_img.append(
                            {f"{y['chapter']}": preaderarea}
                        )
                else:
                    return FinalOutput().results(
                        None,
                        f"the number of limits entered is too much! count: {information['chapter_count']} Chapter only",
                        400,
                    )
            return FinalOutput().results(self._ReadComic__data_img, "success", 200)

    def getInfo(self) -> list:
        soup = self._Main__Response("info")
        info = soup.find("div", attrs={"class": "info-right"})
        info_comic = info.findAll("div", attrs={"class": "wd-full"})
        title, genres, sinopsis = (
            info_comic[1].find("h2").string,
            [x.string for x in info_comic[0].find("span").findAll("a")],
            info_comic[1]
            .find("div", attrs={"itemprop": "description"})
            .find("p")
            .string,
        )
        data = soup.findAll("div", attrs={"class": "inepcx"})[1].find("a").get("href")
        data_chapters = soup.findAll("li", attrs={"data-num": True})
        for x in data_chapters:
            data_chapter = url, chapter, chapter_release = [
                x.find("a").get("href"),
                x.find("span", attrs={"class": "chapternum"}).text,
                x.find("span", attrs={"class": "chapterdate"}).text,
            ]
            self._ReadComic__data_chapter.append(
                {
                    "url": url,
                    "chapter": chapter,
                    "releases_date": chapter_release,
                }
            )
        count_chapter = int(
            re.findall(
                ".*?chapter\-(\d+).*?",
                str(data),
            )[0]
        )
        self._ReadComic__data_chapter.reverse()
        self._ReadComic__data_list.append(
            {
                "title": title,
                "genres": genres,
                "sinopsis": sinopsis,
                "chapter_content": self._ReadComic__data_chapter,
                "chapter_count": count_chapter,
            }
        )
        return self._ReadComic__data_list
