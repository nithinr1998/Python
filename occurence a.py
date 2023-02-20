list =['alan','adona','nithin','shyam']
print(list)
str = ""
for i in list:
    str = str + i
count = 0
for i in range(len(str)):
    if str[i] == "a":
        count = count+1
print("Count of a :",count)
