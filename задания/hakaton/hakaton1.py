from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://www.mashina.kg/')

count = 0
def pars_html(url: str) -> str: 
    response = requests.get(url)
    return response.text

def pars_bs(html: str):
    BS = BeautifulSoup(html, 'html_parser')
    return BS

def pars_data(soup: BeautifulSoup) -> list:
    data = soup.find('div', class_='table-view-list image-view clr label-view')
    tachki = data.find_all('div', class_='list-item list-label')
    res = []
    for tachka in tachki:
        marka = tachka.find('h2', class_='name')
        image = tachka.find('img', class_='tmb-wrap-table')
        price_block = tachka.find('div', class_='block price')
        price = price_block.find('p'), ('strong')
        year_miles = tachka.find('p', class_='year-miles')
        body_type = tachka.find('p', class_='body-type')
        volume = tachka.find('p', class_='volume')
        list_ = [year_miles, body_type, volume]
        about_car = ', '.join(tachka.find('p', class_=x).text.strip() for x in list_)
        print(about_car)
        res_ = {
            'marka': marka,
            'image': image,
            'price': price,
            'about_car': about_car
        } 
        res.append(res_)

        return res
def file_csv() -> None:
    with open('hakaton.csv', 'w') as file:
        fieldnames = ['Marka', 'Image', 'Price', 'About_car']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            'Marka': 'Marka',
            'Price': 'Price',
            'Image': 'Image',
            'About_car': 'About_car'

        })

def file_csv_write(res_: dict) -> None:
    with open('hakaton.csv', 'a') as file:
        fieldnames = ['Marka', 'Price', 'Image', 'About_car']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for tachka in res_:
            writer.writerow({
                'Marka': tachka['marka'],
                'Image': tachka['image'],
                'Price': tachka['price'],
                'About_car': tachka['about_car']
                })
            count += 1

def main():
    i = 1
    file_csv()
    url = 'https://www.mashina.kg/commercialsearch/all/?page={i}'
    html = pars_html(url)   
    soup = pars_bs(html)
    data = pars_data(soup)
    file_csv_write(data)
    print(f'спарсиди  всего {i} страниц ')

main()