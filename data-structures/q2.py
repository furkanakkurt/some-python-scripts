def inputProducts(names, prices):
    name = str(input("Enter the name of the food: "))
    price = float(input("Enter the price of the food: "))
    while name != "quit":
        names.append(name)
        prices.append(price)    
        name = str(input("Enter the name of the food: "))
        price = float(input("Enter the price of the food: "))

def maxPrice(prices):
    index = 0
    maxPrice = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > maxPrice:
            maxPrice = prices[i]
            index = i
    return index

def minPrice(prices):
    index = 0
    minPrice = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
            index = i
    return index

def find_results(names, prices, function_name):
    index = function_name(prices)
    return (names[index], prices[index])

items = []
prices = []

inputProducts(items, prices)

v1,v2 = find_results(items, prices, maxPrice)

v3, v4 = find_results(items, prices, minPrice)
print('Item with highest price:',v1,'price:',v2)
print('Item with lowest price:',v3,'price:',v4)