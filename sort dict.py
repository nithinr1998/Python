y = {'Alex':20, 'Nithin': 23, 'Philip': 22, 'Shyam': 25}
l = list(y.items())
print('Ascending :', l)
l.sort(reverse=True)
print('Descending :', l)
dict = dict(l)
print("Dictionary", dict)
