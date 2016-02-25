__author__ = 'Hernan Y.Ke'
prices = {
    'A': 100,
    'B': 10,
    'C': 20,
    'D': 50
}

print(max(prices))  #max key name
print(max(prices.values())) #max value name
print(max(prices, key=lambda x: prices[x])) #max value's corresponding key
print(prices[max(prices, key=lambda x: prices[x])])#max value's name

#zip
pn = zip(prices.keys(),prices.values())
print(min(pn)) #iterators can be only consumed once.
print(max(pn))