from .models import PostalCode
# @api_view(['GET'])
# def get_address_by_zip(request,zipcode):

import json
def updateNepal_postal_codes():
    f =open('../nepal_postal_code.json')
    data=json.load(f)
    for i in data:

        postalcode=PostalCode()
        setattr(postalcode,k,v)
        postalcode.save()
updateNepal_postal_codes()