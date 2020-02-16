""" get the content of listing """
import requests
from bs4 import BeautifulSoup


class Check_listing():
    def __init__(self):
        pass

    def request_data(self, url):
        req = requests.get(url)
        return self._process_data(BeautifulSoup(req.content))

    def _process_data(self, content):
        try:
            print('success')
            company = content.findAll(
                "a", {"class": "topcard__org-name-link topcard__flavor--black-link"})[0].string
            description = content.findAll(
                "div", {"class": "description__text description__text--rich"})[0].text
            return (company)
        except IndexError:
            print('\nFailed', content.title())
