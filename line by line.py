#a Python program to read a file line by line and store it into a list.
#  using readlines()

# without strip()
f=open("file.txt",'r')
file_lines=f.readlines()
print(file_lines)
f.close()

# By using strip()
print("\n File content after removing newline character: ")
stripped_lines=[x.strip() for x in file_lines]
print(stripped_lines)
f.close()
