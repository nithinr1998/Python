total = 0
mylist=[]
while(True):
   val = int(input("Enter the numbers to be inserted to list: "))
   mylist.append(val)
   choice = input("Type yes to stop INSERTING else other keys: ")
   if (choice == "yes"):
      break

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(mylist)):
    total = total + mylist[ele]

# printing total value
print("Sum of all elements in given list: ", total)
