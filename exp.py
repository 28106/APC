try :
    n = 0
    res = 100/n
except zeroDivisionError:
    print("You Can't divide by zero!")
else:
    print("Result is:", res)
finally:
    print("Execution Complete")


try:
    Value = int(input("Enter a Number:"))
    # return Value
except ValueError:
    print("Value Division Error")
else:
    print("Value is:", Value)
finally:
    print("Exception Complete")


try:
    file1 = open("example.txt","r")
except FileNotFoundError:
    print("File Not Found Error")
else:
    print("File Opened Successfully!")
    file1.close()
finally:
    print("Execution Complete")


try:
    n = int(input("Enter A Number:"))
except KeyboardInterrupt:
    print("Input Canceled by the user")
else:
    print("Number entered by user is:", n)
finally:
    print("Execution Complete")


