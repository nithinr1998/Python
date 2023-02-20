num=int(input("Enter the limit:"))
list1=[]
for i in range(num):

    a=int(input("Enter the element:"))
    list1.append(a)
newlist=[i*i for i in list1 if i>0]
print("The squares",newlist)
