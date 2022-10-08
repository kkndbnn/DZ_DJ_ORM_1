import csv
from pprint import pprint
from phones.models import Phone

with open('phones.csv', encoding='cp1251') as file:
    list_info = []
    reader = csv.reader(file)
    for row in list(reader)[1:]:

        items = row[-1].split(';')
        list_info.append({'name': items[1],
                          'image': items[2],
                          'price': items[3],
                          'release_date': items[4],
                          'lte_exists': items[5]})

def handle(list_info):
    list_info = list_info
    for item in list_info:
        phone = Phone(
            name = item['name'],
            price = item['price'],
            image = item['image'],
            release_date = item['release_date'],
            lte_exists = item['lte_exists']
                  )
        phone.save()