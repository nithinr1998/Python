year=int(input("Enter the year upto which do you want to print leap years:"))
i=2022
while year>=i:
    if(i%4==0):
        print(i)
    i=i+1