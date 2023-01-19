n=int(input("Enter the limit:"))
list=[]
for i in range(n):
    num=int(input("Enter the number:"))
    list.append(num)
sum=0
for i in list:
    sum=sum+i
print("Total=",sum)