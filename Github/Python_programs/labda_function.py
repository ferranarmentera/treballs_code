items = [
    ("product1", 9),
    ("product2", 15),
    ("product3", 12)
]


items.sort(key=lambda item: item[1])
print(items)
# def sort_item(item):
# return item[1]
