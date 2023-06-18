from src.Latip176.module import *


def proxy():
    r = requests.Session()

    response = BeautifulSoup(r.get("https://free-proxy-list.net/").text, "html.parser")

    table = response.find("section", attrs={"id": "list"}).find("table")

    head = [x.text for x in table.find("thead").findAll("th")]
    data = [
        {k: v.text for k, v in zip(head, row.findAll("td"))}
        for row in table.find("tbody").findAll("tr")
    ]

    sorting = [
        {k: v if d["Google"] == "yes" else "Nope" for k, v in d.items()} for d in data
    ]

    return sorting
