arrayOfProducts = [
    {'product': 't-shirt', 'price': 100, 'date': '12-01-2025', 'status': 'active'},
    {'product': 'jeans', 'price': 1200, 'date': '15-02-2025', 'status': 'active'},
    {'product': 'jacket', 'price': 2500, 'date': '18-03-2025', 'status': 'inactive'},
    {'product': 'shoes', 'price': 1800, 'date': '22-04-2025', 'status': 'active'},
    {'product': 'cap', 'price': 250, 'date': '10-05-2025', 'status': 'inactive'},
    {'product': 'hoodie', 'price': 1500, 'date': '30-06-2025', 'status': 'active'},
    {'product': 'shorts', 'price': 700, 'date': '05-07-2025', 'status': 'active'},
    {'product': 'socks', 'price': 150, 'date': '14-08-2025', 'status': 'inactive'},
    {'product': 'belt', 'price': 300, 'date': '20-09-2025', 'status': 'active'},
    {'product': 'watch', 'price': 3200, 'date': '01-10-2025', 'status': 'inactive'},
]

# list(lambda x: x * x)
# list(filter(lambda x : x * x))
# list(map(lambda x: x ** 2, nums)) || map(function, iterable)
# from functools import reduce
# reduce(function, iterable)


data_1 = list(map(lambda x : x['price'] * 10, arrayOfProducts))
# print(data_1)

# new x = {old x, updating price value}
# **x = unpacking
# old price = new price
updated_products = list(map(lambda x: {**x, 'price': x['price'] * 10}, arrayOfProducts))
# print(updated_products)

# print('start')
c1 = 0
while c1 < len(arrayOfProducts):
    # print('process')
    arrayOfProducts[c1]['price'] = arrayOfProducts[c1]['price'] * 100; c1 += 1

# print('end')
print(arrayOfProducts)