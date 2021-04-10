days=set(['mon','tue','wed','thu','fri','fri','sat','sun'])
print(days)
print(type(days))
	
i=iter(days)
print(next(i))

print('-----------')
for d in days:
	print(d)
	
print('mon' in days)

a=set('hvgbjhgbsgfrvb')
print(a)

b=set('shdgfybagyfgbfyg')
print(a-b)
print(a|b)
print(a&b)
print(a^b)