from bs4 import BeautifulSoup
import urllib
f=open('countries.html')
soup=BeautifulSoup(f.read(),'html.parser')
table=(soup.table)
def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)  
        try:
            a=(tr.find('img'))   
            # print(a['srcset'])  
        except:
            print("NONE")
        rowdata= [td.get_text(strip=True) for td in tr.find_all(coltag) ]
        if a is not None:
            rowdata.append(a['src'])
            # rowdata.extend([a['src'],a['srcset']])
        return rowdata
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row

        rows.append(rowgetDataText(tr, 'td') ) # data row       https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
    return rows
data=tableDataText(table)
i=0
json_data=[]
for country in data:
    
    # print( (country[5]))
    if len(country)>6 :
        i+=1
        print(i)
        print(country[6])
        d={}
        d['name']=country[0]
        d['area']=country[1]
        d['percentage']=country[2]
        d['date']=country[3]
        d['population']=country[4]
        d['flag']=country[6]
        json_data.append(d)
        # d['flag_img']=country[7]
        print(d)
    # print(country)
    # for d in country:
    #     print(d)
    

import json
# Write Json 
with open("country_data.json", "w") as file:
    json_object = json.dumps(json_data, indent = 4)
    file.writelines(str(json_object))
    file.close