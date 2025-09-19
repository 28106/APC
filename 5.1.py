# 1. Write a program to building a simple student 
# grade management system for a class of students. 
# The system will store student names and their 
# grades (both as lists) and should be able to 
# perform the following operations:

# Add a new student and their grade.

# Update the grade of an existing student.

# Remove a student from the list.

# Calculate and display the average grade of the class.

# Display the highest and lowest grades in the class.
    

students = []
grades = []

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add a new student and grade")
    print("2. Update a student's grade")
    print("3. Remove a student")
    print("4. Calculate average grade")
    print("5. Display highest and lowest grade")
    print("6. Display all students and grades")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        students.append(name)
        grades.append(grade)
        print("Student added successfully.")

    elif choice == 2:
        name = input("Enter student name to update: ")
        if name in students:
            index = students.index(name)
            grades[index] = float(input("Enter new grade: "))
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name to remove: ")
        if name in students:
            index = students.index(name)
            students.pop(index)
            grades.pop(index)
            print("Student removed successfully.")
        else:
            print("Student not found.")

    elif choice == 4:
        if grades:
            avg = sum(grades) / len(grades)
            print("Average grade:", avg)
        else:
            print("No students in the list.")

    elif choice == 5:
        if grades:
            print("Highest grade:", max(grades))
            print("Lowest grade:", min(grades))
        else:
            print("No students in the list.")

    elif choice == 6:
        if students:
            print("\nStudents and their grades:")
            for i in range(len(students)):
                print(students[i], "-", grades[i])
        else:
            print("No students in the list.")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")


# 3.Write a program to design a configuration system 
# for a web server where some configuration settings 
# should not be changed during runtime, while others 
# can be updated. The server settings are as follows:

# server_ip: A tuple representing the IP address of the server, which should remain unchanged.

# allowed_ips: A list of IP addresses allowed to connect to the server, which can be updated during runtime.

# Write a program that:

# Allows updating the allowed_ips list.

# Prevents updating the server_ip tuple.

# Displays the updated configuration.
# Initial server configuration
server_ip = ("192", "168", "1", "1")  # tuple (unchangeable)
allowed_ips = ["192.168.1.10", "192.168.1.20"]  # list (changeable)

while True:
    print("\n--- Web Server Configuration ---")
    print("1. View configuration")
    print("2. Add allowed IP")
    print("3. Remove allowed IP")
    print("4. Try to update server_ip")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Server IP:", ".".join(server_ip))
        print("Allowed IPs:", allowed_ips)

    elif choice == 2:
        new_ip = input("Enter new allowed IP: ")
        if new_ip not in allowed_ips:
            allowed_ips.append(new_ip)
            print("IP added successfully.")
        else:
            print("IP already in allowed list.")

    elif choice == 3:
        rem_ip = input("Enter IP to remove: ")
        if rem_ip in allowed_ips:
            allowed_ips.remove(rem_ip)
            print("IP removed successfully.")
        else:
            print("IP not found in allowed list.")

    elif choice == 4:
        print("Error: server_ip is read-only and cannot be updated!")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

# 5.Write a program to build a simple text analysis 
# tool. The tool should perform the following 
# operations on a given paragraph of text:

# Count the total number of words.

# Count the frequency of each word.

# Identify and display the top 3 most frequent words.

# Count the number of vowels in the entire text.

text = input("Enter text: ").lower()

words = text.split()
print("Total words:", len(words))


freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print("Word frequency:", freq)


count = 0
print("Top 3 words:")
for word in sorted(freq, key=freq.get, reverse=True):
    print(word, "-", freq[word])
    count += 1
    if count == 3:
        break


vowels = "aeiou"
v_count = 0
for ch in text:
    if ch in vowels:
        v_count += 1
print("Total vowels:", v_count)
