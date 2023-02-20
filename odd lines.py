#program to copy odd lines of one file to another

#opening files for reading and writing data

input_file=open("file.txt",'r')
output_file=open("writedata.txt",'w')

#copying contents from readed file

copy_data=input_file.readlines()
print("\n Actual file content is")
print(copy_data)
for i in range(0,len(copy_data)):
    if i%2==0:
        output_file.write(copy_data[i])
    else:
        pass
#closing file after writing
output_file.close()

#opening write file in read mode and printing values

output_file=open("writedata.txt",'r')
print("odd lines are")
print(output_file.read())

#closing files
input_file.close()
output_file.close()
