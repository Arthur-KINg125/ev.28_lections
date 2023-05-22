from bs4 import BeautifulSoup
import requests
import csv

count = 0
def get_html(url: str) -> str:
    '''Получает html разметку сайта по url'''
    response = requests.get(url)
    return response.text

def get_soup(html: str):
    '''Получает html разметку и структурирует ее в bs'''
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_last_page(soup: BeautifulSoup) -> int:
    '''Функция которая возвращяет последнюю страницу на сайте!'''
    pages = soup.find('ul', class_='pagination').find_all('a', class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)


def get_data(soup: BeautifulSoup) -> list:
    '''Функция которая поулчает нужные данные с сайта mashina.kg и возвращает в виде листа'''
    container = soup.find('div', class_="tab        le-view-list")
    cars = container.find_all('div', class_='list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_='name').contents[0].strip()
        try:
            img = car.find('img', class_='lazy-image').get('data-src')
        except:
            img = 'No image!'
        price_div = car.find('div', class_='block price')
        price = price_div.find('p').find('strong').text
        ls = ['year-miles', 'body-type', 'volume']
        desc = ', '.join(car.find('p', class_=x).text.strip() for x in ls)
        print(desc)
        data = {
            'name': name,
            'desc': desc,
            'price': price,
            'img': img,
            
        }
        result.append(data)
    
    return result
def prepare_csv() -> None:
        '''функция которая подготавливает csv файл!'''
        with open('cars.csv', 'w') as file:
            fieldnames = ['Number', 'Name', 'Description', 'Price', 'Image Url']
            writer = csv.DictWriter(file, fieldnames)
            writer.writerow({
                'Number': 'Number',
                'Name': 'Name',
                'Price': 'Price',
                'Description': 'Description',
                'Image Url': 'Image Url'
            })

def write_to_csv(data: dict) -> None:
    '''Записывает все данные в csv файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['Number', 'Name', 'Description', 'Price', 'Image Url']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for car in data:
            writer.writerow({
                'Number': count,
                'Name': car['name'],
                'Description': car['desc'],
                'Price': car['price'],
                'Image Url': car['img']
            })
            count += 1

def main():
    i = 1
    prepare_csv()

    while True:
        url = 'https://www.mashina.kg/search/all/?page={i}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)     
        data = get_data(soup)
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 15:
            break
        i += 1

main()



