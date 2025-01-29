from bs4 import BeautifulSoup
from requests import get
from re import findall


class JobCampinas:
    def __init__(self, job_title: str = "") -> None:
        self.job_listings = []
        self.job_page = []
        self.job_title = job_title

    def clear(self, txt: str) -> str:
        return str(txt).replace("\n", "").replace("\t", "").replace("\b", "")

    def encode_spaces(self, txt: str) -> str:
        return str(txt).replace(" ", "+")

    def fetch_job(self) -> None:
        for job_listing in self.job_page.findAll(class_="thumbnail"):
            try:
                self.extract_job_information(job_listing["href"])
            except Exception as erro:
                print(f"Erro ao extrair informações do job: {erro}")
                break

    def extract_job_information(self, url: str) -> None:
        link = url
        page = BeautifulSoup(get(url, timeout=30).text, "lxml")
        html = page.find(class_="col-lg-8 conteudo-vaga")

        details = []
        details.append(self.clear(html.h1.span)[16:-16])

        for count, topic in enumerate(html.findAll("p")):
            if count == 2 or count == 3 or count == 4 or count == 5 or count == 6:
                details.append(topic.text)
            elif count >= 7:
                try:
                    self.check_email_and_phone_validity(details, topic.text)
                except Exception as erro:
                    print("SEM CONTATO", erro)
        jobs = {
            "vaga": details[0],
            "salario": details[3][8:],
            "beneficios": details[4][11:],
            "detalhes": details[1][19:],
            "requisito": details[2][12:],
            "contato": details[6],
            "link": link,
        }
        self.job_listings.append(jobs)

    def check_email_and_phone_validity(self, details: list, txt: str) -> None:
        email_phone_regex_patterns = [
            "^([1-9]{2}) 9[7-9]{1}[0-9]{3}-[0-9]{4}$",
            "[a-zA-Z0-9]+[a-zA-Z0-9_.-]+@{1}[a-zA-Z0-9_.-]*\\.+[a-z]{2,4}",
        ]
        for type_index in range(2):
            try:
                details.append(findall(email_phone_regex_patterns[type_index], txt)[0])
            except Exception as erro:
                print(f"Erro ao extrair informações de contato: {erro}")
                pass

    def navigate_jobs(self, count: int) -> None:
        url = "http://empregacampinas.com.br/page/{}/?s={}".format(
            count, self.encode_spaces(self.job_title)
        )
        self.job_page = BeautifulSoup(get(url, timeout=30).text, "lxml")
        self.fetch_job()
