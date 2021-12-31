products = {"Grape":5.9, "Guava": 4.5,
            "Mango":4.8, "Cashew":2.4,
            "Banana":3.0, "Pear": 5.8}

for pro, price in products.items():
    print(pro, " = ", price)
cost = 0
while True:
    pro = input("Select product (n=nothing): ")
    if pro == 'n':
        break
    qty = int(input("Number of product? "))
    cost += products[pro]*qty

print("Price of product(s): ",cost)