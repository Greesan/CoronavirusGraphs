
import pandas as pd;
import requests
import urllib.request
from bs4 import BeautifulSoup

result = requests.get("https://www.worldometers.info/coronavirus/")

 #print(result.status_code)

 #print(result.headers)

src = result.content

soup= BeautifulSoup(src, 'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')
for tr in table_rows:
 	td = tr.find_all('td')
 	row = [i.text for i in td]
 	#print(row)


print("\n")

for tr in table_rows:
 	td = tr.find_all('td')
 	row = [i.text for i in td]
 	if row != []:
 		print(row[1])
 		print(row[2])
 		print(row[3])


#def new_deaths(tag):
#	return tag.has_attr()
#dfs = pd.read_html('https://www.worldometers.info/coronavirus/', header = 0)
#for df in dfs:
#	print(df)