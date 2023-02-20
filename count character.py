#Count the number of characters in a string
text = str(input("Enter your text :"))
list2 = list(text)
print(list2)
count = 0
set1 = set(list2)
abc = len(list2)
for i in set1:
    for j in range(0,abc):
        if i == list2[j]:
            count =count+1
    print("count of ",i,"is",count)
    count = 0
