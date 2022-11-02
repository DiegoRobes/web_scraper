import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Hugo_Award_for_Best_Novel"

info = requests.get(url)
text = info.text

soup = BeautifulSoup(text, 'html.parser')
rows = soup.find_all('tr', attrs={'style': 'background:#B0C4DE;'})

names = []
for i in rows:
    names.append(i.getText().split('\n'))

for i in names:
    while '' in i:
        i.remove('')

for index, item in enumerate(names):
    if len(item) == 1:
        names[index - 1].insert(2, item[0])
        names.remove(item)

    if len(item) == 4:
        item.insert(0, names[index - 1][0])

for i in names:
    del i[-2:]

del names[-8:]

clean = []
for x in names:
    year = list(i.replace('*', '').replace('[c]', '').replace('[e]', '').replace('[f]', '') for i in x)
    clean.append(year)

for i in clean:
    if len(i) == 4:
        i[1] += ' & ' + i[2]
        del i[2]

fields = ['YEAR', 'AUTHOR(S)', 'NOVEL']
with open('Hugo Award Winners.csv', 'w') as doc:
    write = csv.writer(doc)
    write.writerow(fields)
    write.writerows(clean)
