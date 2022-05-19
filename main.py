from bs4 import BeautifulSoup
import requests
import csv
from docxtpl import DocxTemplate
import re
from pprint import pprint

values_list = []
names_list = []
my_list_all = ['Полное название', 'Короткое название', 'ИНН', 'ОГРН', 'КПП',
               'Дата регистрации', 'Юридический адрес', 'Генеральный директор',
               'Учредители', 'Форма', 'Уставный капитал', 'Дата регистрации',
               'Налоговая', 'Адрес налоговой', 'Регистрационный номер в ПФР',
               'Дата регистрации', 'Наименование территориального органа',
               'Регистрационный номер ФссРФ', 'Дата регистрации',
               'Наименование территориального органа']
HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.'
              '2.528119004.1639149415; _gid=GA1.2.512914915.'
              '1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru;'
              ' _ym_isad=2; __gads=ID=87f529752d2e0de1-'
              '221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}
all_requisites = 'https://www.tinkoff.ru/business/contractor/legal/1154253005466/requisites/'

def requisites():
    url = 'https://www.tinkoff.ru/business/contractor/legal/1187746633425/requisites/'
    page = requests.get(url, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    # z = soup.find_all('span', class_='emz9Oe')
    # y = soup.find_all('div', class_='fmz9Oe')
    z = soup.find_all('div', class_='dmz9Oe')
    y = soup.find_all('div', class_='gmz9Oe')
    # print(y)
    for t in y:
        values_list.append(t.text.strip().replace('\xa0',' ').replace('\n','').replace('\r',''))
    for x in z:
        names_list.append(x.text.strip().replace('\n','').replace('\xa0','').replace('\r',''))
    for i in names_list:
        if i == "":
            names_list.remove(i)
    # print(len(names_list))
    # print(len(values_list))

def csv_w():
    with open("data.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        file_writer.writerow(names_list)
        file_writer.writerow(values_list)

def word():
    doc = DocxTemplate("testing.docx")
    # context = {'ИНН': union_dict(), 'ogrn': '222222','ggg': 'fjsngfnjkd'}
    context = union_dict()
    doc.render(context)
    doc.save("test.docx")

def union_dict():
    if len(names_list) == len(values_list):
        my_dict = dict(zip(names_list, values_list))
        return my_dict
    else:
        a = len(values_list) - len(names_list)
        b = []
        print(a)
        print(names_list[8])
        for i in range(a+1):
            k = 8 + i
            b.append(values_list[k])
        print(b)

requisites()
print(union_dict())

