
import requests
from bs4 import BeautifulSoup
 
 
# # Making a GET request
# r = requests.get('http://postalservice.gov.np/detail/postal-codes-of-nepal')

# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# # print(soup.prettify())
# table=(soup.table)
# # rows = table.findAll(lambda tag: tag.name=='tr')

# # def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
# #         return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
# # rows = []
# # trs = table.find_all('tr')
# # headerow = rowgetDataText(trs[0], 'th')


def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows

# data=(tableDataText(table))
# json_data=[]
# for i in data:
#     d=dict()
#     d["district"]=i[0]
#     d["post_office"]=i[1]
#     d["postal_pin_code"]=i[2]
#     d["post_office_type"]=i[3]
#     json_data.append(d)
# # print(json_data)
# import json
# # print(data)
# with open("nepal_postal_code.json", "w") as file:
#     json_object = json.dumps(json_data, indent = 4)
#     file.writelines(str(json_object))
#     file.close

# Districts by province nepal


r = requests.get('https://topnepali.com/districts-in-nepal')
soup=BeautifulSoup(r.content, 'html.parser')
provinces=["Koshi Province(Provice no. 1)"
,"Madesh Province(Province no. 2)",
"Bagmati Province (Province no. 3)",
"Gandaki Province (Province no. 4)",
"Lumbini Province (Province no. 5)",
"Karnali Province (Province no. 6)",
"Sudur-Paschim Province (Province no. 7)"]
table=(soup.table)
data=(tableDataText(table))
data.pop(0)
provinces_districts=[]
for d in data:
    provinces_districts.append((provinces[0],d[1]))
    print(d[1])
list=soup.find_all("ol")
# print(list)

 
for a in range(0,6):
    # print(a.getText(strip=True))
    # provinces_districts.append(list[a].find_all('li'))
    for d in list[a].find_all('li'):
        provinces_districts.append((provinces[a+1],d.get_text()))
    # print(str(list[a])+"\n\n")


# Koshi Province(Provice no. 1)


# Madesh Province(Province no. 2)
# Bagmati Province (Province no. 3)
# Gandaki Province (Province no. 4)
# Lumbini Province (Province no. 5)
# Karnali Province (Province no. 6)
# Sudur-Paschim Province (Province no. 7)




print(provinces_districts)
print(len(provinces_districts))

json_data=[]
for i in provinces_districts:
    d=dict()
    d["province"]=i[0]
    d["district"]=i[1] 
    json_data.append(d)
print(json_data)
import json
# Write Json 
# with open("province_districts.json", "w") as file:
#     json_object = json.dumps(json_data, indent = 4)
#     file.writelines(str(json_object))
#     file.close


