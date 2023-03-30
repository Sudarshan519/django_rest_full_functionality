from selenium import webdriver
import time
url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
driver = webdriver.Firefox()
driver.get(url)#"https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
time.sleep(3)
print(driver.page_source)
# print(driver.page_source)
# from selenium import webdriver
# browser = webdriver.Firefox()
from bs4 import BeautifulSoup
# browser.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
soup = BeautifulSoup(driver.page_source, "html.parser")
table=(soup.find('table',{"class":"wikitable sortable static-row-numbers plainrowheaders srn-white-background jquery-tablesorter"}))
# import requests




def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        # return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
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
# r = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population/')
# print(r.content)

# # import json
# # print(data)
with open("countries_by_gdp.html", "w") as file:
    # json_object = json.dumps(json_data, indent = 4)
    file.writelines(str(table))
    file.close

# soup=BeautifulSoup(r.content, 'html.parser')
# table=(soup.table)

data=(tableDataText(table))
print(data)