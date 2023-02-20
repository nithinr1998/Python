mylist = [100,101,102,103,104,105,106]
print(mylist)
for i in mylist:
    if i%2==0:
        mylist.remove(i)
print(mylist)
