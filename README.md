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