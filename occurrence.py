a=input("Enter your list:")
list=a.split(" ")
print(list)
count=0
for i in list:
    for k in list:
        if(i==k):
            count=count+1
    print(count)
    count=0