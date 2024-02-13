list1 = [1, 'sloth', '3081', 'four']
list2 = [4, 'baby', 1, 'four']
def intersection(a, b):
    s = list(filter(lambda x: x in a, b))
    return s
print(intersection(list1, list2))