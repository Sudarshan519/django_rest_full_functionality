# django_rest_full_functionality


# Calculate the total amount for all products with their quantities
total_amount = Product.objects.annotate(
    total_quantity=Sum('order__quantity'),
    total_amount=ExpressionWrapper(
        F('total_quantity') * F('price'),
        output_field=DecimalField(max_digits=10, decimal_places=2)
    )
).aggregate(
    total_amount=Sum('total_amount')
)['total_amount']


# Get a list of products with their total prices for the specific user
product_list = Order.objects.filter(order__user=user).annotate(
    total_price=Sum(F('order__quantity') * F('price'))
)


pip install -U googlemaps


import googlemaps

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# Create a Google Maps client
gmaps = googlemaps.Client(key=api_key)

# Perform a place search
places = gmaps.places(query="restaurants in New York", language="en", location=(40.7128, -74.0060), radius=1000)

# Print the results
for place in places['results']:
    print(f"Name: {place['name']}")
    print(f"Address: {place.get('vicinity', 'N/A')}")
    print(f"Rating: {place.get('rating', 'N/A')}")
    print("-----")
