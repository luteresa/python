shoplist = ['apple','manggo','carrot','banana']
print('I have', len(shoplist), ' items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
	print(item,end=' ')
print('\nI alse bave to buy rice.')
shoplist.append('rice')
print('My shopping list is now:',shoplist)

print('I will sort my list now.')
shoplist.sort()
print('My shopping list is now:',shoplist)

print("The first item I will buy is",shoplist[0])


olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)

print('My shopping list is now:',shoplist)
