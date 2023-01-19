n=int(input("Enter the limit:"))
list=[]

for i in range(n):
    num=int(input("Enter the number:"))
    if num>100:
        num="over"
    list.append(num)
print(list)

