print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist

#I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)

print('Copy by making a full slice')
mylist2=shoplist[:]
del mylist2[0]

print('shoplist is',shoplist)
print('mylist is',mylist)
print('mylist2 is',mylist2)
