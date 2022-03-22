# This is a sample Python script.

import json
import statistics
from urllib.parse import unquote
import requests
from selectolax.parser import HTMLParser
statistics


def get_json(url):
    data = {}

    response = requests.get(url=url)
    html = response.text

    tree = HTMLParser(html)
    scripts = tree.css('script')
    for script in scripts:
        if 'window.__initialData__' in script.text():
            jsontext = script.text().split(';')[0].split('=')[-1].strip()
            jsontext = unquote(jsontext)
            jsontext = jsontext[1:-1]

            data = json.loads(jsontext)

    return data

def get_offers(data):
    offers = []
    for key in data:
        if 'single-page' in key:
            items = data[key]["data"]["catalog"]["items"]
            for item in items:
                if item.get("id"):
                    offer = item["normalizedPrice"]
                    offers.append(offer)

    return offers


def main():
     url = 'https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?s=104'
     data = get_json(url)
     offers = get_offers(data)
     for offer in offers:
        
         print(offer)




if __name__ == '__main__':
    main()
