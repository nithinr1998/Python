n=int(input("Enter the limit:"))
list=[]
for i in range(n):
    num=input("Enter the string:")
    list.append(num)

maximum = len(list[0])
temp = list[0]

for i in list:
    if (len(i) > maximum):
        maximum = len(i)
        temp = i
print("Longest word is", temp," and length is ", maximum)