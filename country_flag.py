from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
time.sleep(2)
# print(driver.page_source)
# from selenium import webdriver
# browser = webdriver.Firefox()
from bs4 import BeautifulSoup
# browser.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population")
soup = BeautifulSoup(driver.page_source, "html.parser")
table=(soup.find('table',{"class":"wikitable sortable jquery-tablesorter"}))
# import requests




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
        rows.append(rowgetDataText(tr, 'td') ) # data row       https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
    return rows
# r = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population/')
# print(r.content)

# # import json
# # print(data)
with open("countries.html", "w") as file:
    # json_object = json.dumps(json_data, indent = 4)
    file.writelines(str(table))
    file.close

# soup=BeautifulSoup(r.content, 'html.parser')
# table=(soup.table)

data=(tableDataText(table))
print(data)
# print(data.pop(0))

# table=(soup.table)
# data=(tableDataText(table))
# print(table)

# def get_flag():
#         flagOffset = 0x1F1E6
#         asciiOffset = 0x41

#         country = "US"

#         firstChar = chr.codePointAt(country, 0) - asciiOffset + flagOffset
#         secondChar = chr.codePointAt(country, 1) - asciiOffset + flagOffset
#         flag =   str(chr.toChars(firstChar))+   str(char.toChars(secondChar))
#         return flag
# get_flag()

# import argparse
# import re
# import json
# from urllib.parse import quote
# from urllib.request import urlopen, Request

# def get_contents(l):
#     url = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvprop=content&redirects=&titles="
#     url += "|".join(quote(i) for i in l)

#     data = json.loads(urlopen(url).read().decode('utf-8'))

#     normalized = {i: i for i in l}
#     if "normalized" in data["query"]:
#         normalized.update({n["from"]: n["to"] for n in data["query"]["normalized"]})
#     redirects = {i: i for i in normalized.values()}
#     if "redirects" in data["query"]:
#         redirects.update({r["from"]: r["to"] for r in data["query"]["redirects"]})
#     contents = {p["title"]: p["revisions"][0]["*"] for p in data["query"]["pages"].values()}

#     return {i: contents[redirects[normalized[i]]] for i in l}




# def getFlags(code){
#     code = strtoupper(code);
#     if(code == 'AD') return '🇦🇩';
#     if(code == 'AE') return '🇦🇪';
#     if(code == 'AF') return '🇦🇫';
#     if(code == 'AG') return '🇦🇬';
#     if(code == 'AI') return '🇦🇮';
#     if(code == 'AL') return '🇦🇱';
#     if(code == 'AM') return '🇦🇲';
#     if(code == 'AO') return '🇦🇴';
#     if(code == 'AQ') return '🇦🇶';
#     if(code == 'AR') return '🇦🇷';
#     if(code == 'AS') return '🇦🇸';
#     if(code == 'AT') return '🇦🇹';
#     if(code == 'AU') return '🇦🇺';
#     if(code == 'AW') return '🇦🇼';
#     if(code == 'AX') return '🇦🇽';
#     if(code == 'AZ') return '🇦🇿';
#     if(code == 'BA') return '🇧🇦';
#     if(code == 'BB') return '🇧🇧';
#     if(code == 'BD') return '🇧🇩';
#     if(code == 'BE') return '🇧🇪';
#     if(code == 'BF') return '🇧🇫';
#     if(code == 'BG') return '🇧🇬';
#     if(code == 'BH') return '🇧🇭';
#     if(code == 'BI') return '🇧🇮';
#     if(code == 'BJ') return '🇧🇯';
#     if(code == 'BL') return '🇧🇱';
#     if(code == 'BM') return '🇧🇲';
#     if(code == 'BN') return '🇧🇳';
#     if(code == 'BO') return '🇧🇴';
#     if(code == 'BQ') return '🇧🇶';
#     if(code == 'BR') return '🇧🇷';
#     if(code == 'BS') return '🇧🇸';
#     if(code == 'BT') return '🇧🇹';
#     if(code == 'BV') return '🇧🇻';
#     if(code == 'BW') return '🇧🇼';
#     if(code == 'BY') return '🇧🇾';
#     if(code == 'BZ') return '🇧🇿';
#     if(code == 'CA') return '🇨🇦';
#     if(code == 'CC') return '🇨🇨';
#     if(code == 'CD') return '🇨🇩';
#     if(code == 'CF') return '🇨🇫';
#     if(code == 'CG') return '🇨🇬';
#     if(code == 'CH') return '🇨🇭';
#     if(code == 'CI') return '🇨🇮';
#     if(code == 'CK') return '🇨🇰';
#     if(code == 'CL') return '🇨🇱';
#     if(code == 'CM') return '🇨🇲';
#     if(code == 'CN') return '🇨🇳';
#     if(code == 'CO') return '🇨🇴';
#     if(code == 'CR') return '🇨🇷';
#     if(code == 'CU') return '🇨🇺';
#     if(code == 'CV') return '🇨🇻';
#     if(code == 'CW') return '🇨🇼';
#     if(code == 'CX') return '🇨🇽';
#     if(code == 'CY') return '🇨🇾';
#     if(code == 'CZ') return '🇨🇿';
#     if(code == 'DE') return '🇩🇪';
#     if(code == 'DJ') return '🇩🇯';
#     if(code == 'DK') return '🇩🇰';
#     if(code == 'DM') return '🇩🇲';
#     if(code == 'DO') return '🇩🇴';
#     if(code == 'DZ') return '🇩🇿';
#     if(code == 'EC') return '🇪🇨';
#     if(code == 'EE') return '🇪🇪';
#     if(code == 'EG') return '🇪🇬';
#     if(code == 'EH') return '🇪🇭';
#     if(code == 'ER') return '🇪🇷';
#     if(code == 'ES') return '🇪🇸';
#     if(code == 'ET') return '🇪🇹';
#     if(code == 'FI') return '🇫🇮';
#     if(code == 'FJ') return '🇫🇯';
#     if(code == 'FK') return '🇫🇰';
#     if(code == 'FM') return '🇫🇲';
#     if(code == 'FO') return '🇫🇴';
#     if(code == 'FR') return '🇫🇷';
#     if(code == 'GA') return '🇬🇦';
#     if(code == 'GB') return '🇬🇧';
#     if(code == 'GD') return '🇬🇩';
#     if(code == 'GE') return '🇬🇪';
#     if(code == 'GF') return '🇬🇫';
#     if(code == 'GG') return '🇬🇬';
#     if(code == 'GH') return '🇬🇭';
#     if(code == 'GI') return '🇬🇮';
#     if(code == 'GL') return '🇬🇱';
#     if(code == 'GM') return '🇬🇲';
#     if(code == 'GN') return '🇬🇳';
#     if(code == 'GP') return '🇬🇵';
#     if(code == 'GQ') return '🇬🇶';
#     if(code == 'GR') return '🇬🇷';
#     if(code == 'GS') return '🇬🇸';
#     if(code == 'GT') return '🇬🇹';
#     if(code == 'GU') return '🇬🇺';
#     if(code == 'GW') return '🇬🇼';
#     if(code == 'GY') return '🇬🇾';
#     if(code == 'HK') return '🇭🇰';
#     if(code == 'HM') return '🇭🇲';
#     if(code == 'HN') return '🇭🇳';
#     if(code == 'HR') return '🇭🇷';
#     if(code == 'HT') return '🇭🇹';
#     if(code == 'HU') return '🇭🇺';
#     if(code == 'ID') return '🇮🇩';
#     if(code == 'IE') return '🇮🇪';
#     if(code == 'IL') return '🇮🇱';
#     if(code == 'IM') return '🇮🇲';
#     if(code == 'IN') return '🇮🇳';
#     if(code == 'IO') return '🇮🇴';
#     if(code == 'IQ') return '🇮🇶';
#     if(code == 'IR') return '🇮🇷';
#     if(code == 'IS') return '🇮🇸';
#     if(code == 'IT') return '🇮🇹';
#     if(code == 'JE') return '🇯🇪';
#     if(code == 'JM') return '🇯🇲';
#     if(code == 'JO') return '🇯🇴';
#     if(code == 'JP') return '🇯🇵';
#     if(code == 'KE') return '🇰🇪';
#     if(code == 'KG') return '🇰🇬';
#     if(code == 'KH') return '🇰🇭';
#     if(code == 'KI') return '🇰🇮';
#     if(code == 'KM') return '🇰🇲';
#     if(code == 'KN') return '🇰🇳';
#     if(code == 'KP') return '🇰🇵';
#     if(code == 'KR') return '🇰🇷';
#     if(code == 'KW') return '🇰🇼';
#     if(code == 'KY') return '🇰🇾';
#     if(code == 'KZ') return '🇰🇿';
#     if(code == 'LA') return '🇱🇦';
#     if(code == 'LB') return '🇱🇧';
#     if(code == 'LC') return '🇱🇨';
#     if(code == 'LI') return '🇱🇮';
#     if(code == 'LK') return '🇱🇰';
#     if(code == 'LR') return '🇱🇷';
#     if(code == 'LS') return '🇱🇸';
#     if(code == 'LT') return '🇱🇹';
#     if(code == 'LU') return '🇱🇺';
#     if(code == 'LV') return '🇱🇻';
#     if(code == 'LY') return '🇱🇾';
#     if(code == 'MA') return '🇲🇦';
#     if(code == 'MC') return '🇲🇨';
#     if(code == 'MD') return '🇲🇩';
#     if(code == 'ME') return '🇲🇪';
#     if(code == 'MF') return '🇲🇫';
#     if(code == 'MG') return '🇲🇬';
#     if(code == 'MH') return '🇲🇭';
#     if(code == 'MK') return '🇲🇰';
#     if(code == 'ML') return '🇲🇱';
#     if(code == 'MM') return '🇲🇲';
#     if(code == 'MN') return '🇲🇳';
#     if(code == 'MO') return '🇲🇴';
#     if(code == 'MP') return '🇲🇵';
#     if(code == 'MQ') return '🇲🇶';
#     if(code == 'MR') return '🇲🇷';
#     if(code == 'MS') return '🇲🇸';
#     if(code == 'MT') return '🇲🇹';
#     if(code == 'MU') return '🇲🇺';
#     if(code == 'MV') return '🇲🇻';
#     if(code == 'MW') return '🇲🇼';
#     if(code == 'MX') return '🇲🇽';
#     if(code == 'MY') return '🇲🇾';
#     if(code == 'MZ') return '🇲🇿';
#     if(code == 'NA') return '🇳🇦';
#     if(code == 'NC') return '🇳🇨';
#     if(code == 'NE') return '🇳🇪';
#     if(code == 'NF') return '🇳🇫';
#     if(code == 'NG') return '🇳🇬';
#     if(code == 'NI') return '🇳🇮';
#     if(code == 'NL') return '🇳🇱';
#     if(code == 'NO') return '🇳🇴';
#     if(code == 'NP') return '🇳🇵';
#     if(code == 'NR') return '🇳🇷';
#     if(code == 'NU') return '🇳🇺';
#     if(code == 'NZ') return '🇳🇿';
#     if(code == 'OM') return '🇴🇲';
#     if(code == 'PA') return '🇵🇦';
#     if(code == 'PE') return '🇵🇪';
#     if(code == 'PF') return '🇵🇫';
#     if(code == 'PG') return '🇵🇬';
#     if(code == 'PH') return '🇵🇭';
#     if(code == 'PK') return '🇵🇰';
#     if(code == 'PL') return '🇵🇱';
#     if(code == 'PM') return '🇵🇲';
#     if(code == 'PN') return '🇵🇳';
#     if(code == 'PR') return '🇵🇷';
#     if(code == 'PS') return '🇵🇸';
#     if(code == 'PT') return '🇵🇹';
#     if(code == 'PW') return '🇵🇼';
#     if(code == 'PY') return '🇵🇾';
#     if(code == 'QA') return '🇶🇦';
#     if(code == 'RE') return '🇷🇪';
#     if(code == 'RO') return '🇷🇴';
#     if(code == 'RS') return '🇷🇸';
#     if(code == 'RU') return '🇷🇺';
#     if(code == 'RW') return '🇷🇼';
#     if(code == 'SA') return '🇸🇦';
#     if(code == 'SB') return '🇸🇧';
#     if(code == 'SC') return '🇸🇨';
#     if(code == 'SD') return '🇸🇩';
#     if(code == 'SE') return '🇸🇪';
#     if(code == 'SG') return '🇸🇬';
#     if(code == 'SH') return '🇸🇭';
#     if(code == 'SI') return '🇸🇮';
#     if(code == 'SJ') return '🇸🇯';
#     if(code == 'SK') return '🇸🇰';
#     if(code == 'SL') return '🇸🇱';
#     if(code == 'SM') return '🇸🇲';
#     if(code == 'SN') return '🇸🇳';
#     if(code == 'SO') return '🇸🇴';
#     if(code == 'SR') return '🇸🇷';
#     if(code == 'SS') return '🇸🇸';
#     if(code == 'ST') return '🇸🇹';
#     if(code == 'SV') return '🇸🇻';
#     if(code == 'SX') return '🇸🇽';
#     if(code == 'SY') return '🇸🇾';
#     if(code == 'SZ') return '🇸🇿';
#     if(code == 'TC') return '🇹🇨';
#     if(code == 'TD') return '🇹🇩';
#     if(code == 'TF') return '🇹🇫';
#     if(code == 'TG') return '🇹🇬';
#     if(code == 'TH') return '🇹🇭';
#     if(code == 'TJ') return '🇹🇯';
#     if(code == 'TK') return '🇹🇰';
#     if(code == 'TL') return '🇹🇱';
#     if(code == 'TM') return '🇹🇲';
#     if(code == 'TN') return '🇹🇳';
#     if(code == 'TO') return '🇹🇴';
#     if(code == 'TR') return '🇹🇷';
#     if(code == 'TT') return '🇹🇹';
#     if(code == 'TV') return '🇹🇻';
#     if(code == 'TW') return '🇹🇼';
#     if(code == 'TZ') return '🇹🇿';
#     if(code == 'UA') return '🇺🇦';
#     if(code == 'UG') return '🇺🇬';
#     if(code == 'UM') return '🇺🇲';
#     if(code == 'US') return '🇺🇸';
#     if(code == 'UY') return '🇺🇾';
#     if(code == 'UZ') return '🇺🇿';
#     if(code == 'VA') return '🇻🇦';
#     if(code == 'VC') return '🇻🇨';
#     if(code == 'VE') return '🇻🇪';
#     if(code == 'VG') return '🇻🇬';
#     if(code == 'VI') return '🇻🇮';
#     if(code == 'VN') return '🇻🇳';
#     if(code == 'VU') return '🇻🇺';
#     if(code == 'WF') return '🇼🇫';
#     if(code == 'WS') return '🇼🇸';
#     if(code == 'XK') return '🇽🇰';
#     if(code == 'YE') return '🇾🇪';
#     if(code == 'YT') return '🇾🇹';
#     if(code == 'ZA') return '🇿🇦';
#     if(code == 'ZM') return '🇿🇲';
#     return '🏳';
# }

