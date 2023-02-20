name = "Nithin Rajappan"
print(name)
abc = name.split(" ")
l1 = list(abc[0])
l2 = list(abc[1])
temp = l1[0]
temp2 = l2[0]
l1[0] =temp2
l2[0] = temp
print("".join(l1))
print("".join(l2))

