d = {'a': 1, 'b': 2}

# get
print(d.get('a'))  # 1
print(d.get('c', 0))  # 0

# update
d.update({'c': 3})

# pop
d.pop('b')  # removes key 'b'

# keys, values, items
print(d.keys())    # dict_keys(['a', 'c'])
print(d.values())  # dict_values([1, 3])
print(d.items())   # dict_items([('a', 1), ('c', 3)])
