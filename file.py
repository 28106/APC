#Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("File handling in Python is easy!\n")

print("File created and written successfully.")

#Reading the file
with open("example.txt", "r") as file:
    print("\nReading file content:")
    content = file.read()
    print(content)

#Appending new content
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

print("New line appended successfully.")

#Reading again to confirm
with open("example.txt", "r") as file:
    print("\nUpdated file content:")
    print(file.read())


