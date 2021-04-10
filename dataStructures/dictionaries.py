d={'name':'Raj','age':22,'place':'Chennai'}
print(d['age'])
print(d['name'])
print(d['place'])
d['country']='India'
print(d)
print(d['country'])
del d['country']
print(d)
print(len(d))
print(str(d))
print(d.fromkeys('name'))

print(d.get('age'))
print(d.items())
print(d.keys())
print(d.values())
