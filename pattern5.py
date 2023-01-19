n=int(input("Enter the size:"))
for i in range(0,n-1):
     for j in range(0,i+1):
         print('*',end='   ')
     print()
for i in range(n,0,-1):
     for j in range(0,i):
          print("*",end='   ')
     print()
