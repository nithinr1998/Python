str=input("enter the string")
a=str[0]

for i in str:
     if(str[0]==i):

         b=str.replace(i,'$')

print(a+b[1:])
