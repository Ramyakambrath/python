from bs4 import BeautifulSoup
import requests
import re


# import csv
url= "C:/python/html/index.html"
html = open(url).read();
# bsObj = BeautifulSoup(re.sub("<!--|-->","", html), "lxml")
soup = BeautifulSoup(html,"lxml")

print(soup.title)
#print(bsObj.table)
# table = bsObj.findAll('table')
# print(table)
# output_rows = []
# for table_row in table.findAll('tr'):
#     columns = table_row.findAll('td')
#     output_row = []
#     for column in columns:
#         output_row.append(column.text)
#     output_rows.append(output_row)
    
# with open('output.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(output_rows)