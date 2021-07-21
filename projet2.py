import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-study-in-scarlet-sherlock-holmes-1_656/index.html'

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')
    col = 0
    for row in rows:
        data = row.find('td')
        if col == 0:
            upc = data.text
        if col == 2:
            price = data.text
        if col == 3:
            pricetax = data.text
        if col == 5:
            availablity = data.text
        col += 1



    print(upc)
    print(price)
    print(pricetax)
    print(availablity)
    
""""
    col = 0
    for p in soup.find_all('p'):
        data = soup.find('p')
        if col == 7:
            product_description = data.text
        col += 1
"""






"""if response.ok:
    source = BeautifulSoup(response.text, 'html.parser')
    tr = source.find_all('tr')
    for tr in source.find_all('tr'):
        col = 0
        for td in tr.find('td'):
            td_text = tr.find('td')
            if col == 0:
                upc = td_text
            if col == 1:
                product = td_text
            if col == 2:
                price = td_text
            if col == 3:
                pricetax = td_text
            col += 1
    print(upc)
    print(price)
    print(pricetax)
"""


"""  
    title = source.find('h1')
    upc = source.find('td')
    print(title.text)
    print(len(upc))
"""