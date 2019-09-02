from collections import OrderedDict

n = int(input())
shop_items = OrderedDict()
for i in range(n):
    data = input().split()
    value=data[-1]
    data.pop(-1)
    key=' '.join(data)
    if key in shop_items.keys():
        shop_items[key] += int(value)
    else:
        shop_items[key] = int(value)
for key, money in shop_items.items():
    print(key, money)
