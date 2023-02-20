list1= [1,2,3,4]
list2= [4,3,2,1]
print(list1)
print(list2)
if len(list1) == len(list2):
    print("List is same length")
else:
    print("List is not of same length")
sum1 = 0
sum2 = 0
for i in list1:
    sum1 = sum1 + i
for i in list2:
    sum2 = sum2 + i
print(sum1)
print(sum2)
if sum1 == sum2:
    print("Sum of two list are same")

else:
    print("Not same sum")
s1 = set(list1)
s2 = set(list2)
print("Common Elements:",s1.intersection(s2))
