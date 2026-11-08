from functools import reduce

prices = [12.5, 99, 56.7, 33, 80.5]

# print([x * 0.8 for x in prices])
# print([x for x in prices if x > 50])
total = sum(prices)
print(total)


print(list(map(lambda x: x * 0.8, prices)))
print(list(filter(lambda x: x > 50, prices)))
print(reduce(lambda a, b: a + b, prices))
