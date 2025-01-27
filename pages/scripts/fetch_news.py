from requests import get
from bs4 import BeautifulSoup


class NewCNNBrasil:
    def __init__(self):
        self.url = "https://www.cnnbrasil.com.br/politica/"
        self.news = []
        self.get_news()

    def get_news(self):
        response = get(self.url)
        html = BeautifulSoup(response.text, "html.parser")
        news = html.find_all("a", class_="home__list__tag")
        for new in news:
            self.news.append(
                {
                    "thumbnail": new.find("img")["src"],
                    "content": new.find("h3").text,
                    "link": new["href"],
                    "date": new.find(class_="home__title__date").text,
                }
            )

    def show_news(self) -> dict:
        return self.news
