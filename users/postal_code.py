from geopy.geocoders import Nominatim
# import country_list

# Using Nominatim Api
geolocator = Nominatim(user_agent="geoapiExercises")
 
def getAddress(code):
    # Zipcode input
    zipcode = "120-0012"
    print(code)
    # Using geocode()
    location = geolocator.geocode(code+",np" )
    print(location.raw)
    location = geolocator.geocode(code ,country_codes=['np'],language=False)#'JP'featuretype=['country', 'state', 'city',]
    
    # Displaying address details
    # print("Zipcode:",zipcode)
    # print("Details of the Zipcode:")
    # print(location[0].split(','))
    # print(location[0].split(',')[0])
    # print(location[0].split(',')[1])
    # print(location[0].split(',')[-4])
    # print(location[0].split(',')[-3])
    # print(location.country)
        # 'street',
        # 'city',
        # 'county',
        # 'state',
        # 'country',
        # 'postalcode',

 
    
    print(location) 
    return location


