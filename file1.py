#create file
f1 = open("sample.txt", "x")
print("File created Successfully!")
f1.close()

#Writing data into file
f1 = open("sample.txt", "w")
f1.write("Hi File Handling in pyhton\n")
f1.write("File Handling is easy in Python\n")
f1.close()


#Reading data 
f1 = open("sample.txt","r")
print("First Line:", f1.readline)
f1.close()

#Read all lines
f1 = open("sample.txt","r")
print("First Line:", f1.readlines)
f1.close()


#Append New Lines
f1 = open("sample.txt","a")
f1.write("This is appended line.\n")
f1.close()


#Binary
f1 = open("sample.txt","wb")
f1.write(b"This is binary data.\n")
f1.close()


#Read & Write
f1 = open("sample.txt", "r+")
print("Before:", f1.read())
f1.seek(0)
f1.write("Updated using 'r+' mode.\n")
f1.close()


#Write & Read
f1 = open("sample.txt", "w+")
f1.write("File updated using 'w+' mode.\n")
f1.seek(0)
print(f1.read())
f1.close()


#Append & Read
f1 = open("sample.txt", "a+")
f1.write("New line added using 'a+' mode.\n")
f1.seek(0)
print(f1.read())
f1.close()






