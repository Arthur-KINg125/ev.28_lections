from bs4 import BeautifulSoup
from requests import get


html = get('https://enter.kg/').text
soup = BeautifulSoup(html, 'html.parser')
container = soup.find('ul', class_='VMmenu')
category_list = [x.text for x in container.find_all('a')]
print(category_list)

def find_category(categories, keyword):
    return [x for x in categories if keyword.lower() in x.lower()]

print(find_category(category_list, 'Ноутбуки'))
