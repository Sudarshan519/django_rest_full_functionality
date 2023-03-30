from unicodedata import lookup


lookup('REGIONAL INDICATOR SYMBOL LETTER n') + lookup('REGIONAL INDICATOR SYMBOL LETTER e')
 
lookup('REGIONAL INDICATOR SYMBOL LETTER i') + lookup('REGIONAL INDICATOR SYMBOL LETTER e')
 
d=(lookup('REGIONAL INDICATOR SYMBOL LETTER n') + lookup('REGIONAL INDICATOR SYMBOL LETTER p'))
print(d)
# OFFSET = ord('🇦') - ord('A')
# def flag(code):
#     return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)
# print(flag('US'))

# OFFSET = ord('🇦') - ord('A')

import iso3166

def flag_emoji(name):
    alpha = iso3166.countries.get(name).alpha2
    box = lambda ch: chr( ord(ch) + 0x1f1a5 )
    return box(alpha[0]) + box(alpha[1])
    print(flag_emoji("Canada"))


def print_all_flags():
    for i, c in enumerate( iso3166.countries ):
        print(flag_emoji(c.name), end="")
        if i%25 == 24: print()
print_all_flags()
"https://flagcdn.com/24x18/${countryCode}.png"
print(len(iso3166.countries))
# for c in iso3166.countries:
#     print(c)