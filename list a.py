
num=int(input("Enter the limit:"))
list1=[]
for i in range(num):
    a=int(input("Enter the element:"))
    list1.append(a)
print("The list you entered is:",list1)
newlist=[i for i in list1 if i>0]
print("New list is",newlist)

