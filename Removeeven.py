n=int(input("Enter the limit:"))
list=[]
for i in range(n):
    num=int(input("Enter the number:"))
    list.append(num)
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print(list)
