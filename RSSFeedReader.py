import requests
from bs4 import BeautifulSoup


class RSSFeedReader(object):

    def __init__(self):
        pass

    def get_data(self, link):
        data = requests.get(link)
        data = BeautifulSoup(data.text, 'html.parser')

        title = data.find_all("title")
        description = data.find_all("description")
        link = data.find_all("link")

        information = list()
        for index in range(0, len(title)):
            information.append([title[index], description[index], link[index]])

        return information


RSS = RSSFeedReader()
