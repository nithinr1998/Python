str=input("Enter the string:")
end1=str[-1:-4]
end2=end1[:-1]

if end1=="ing":
    print(str+'ly')
else:
    print(str+'ing')

