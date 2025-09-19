# 1.check the entered number is prime or not
num = int(input("Enter a number: "))
i = 2
if num <= 1:
    print("Not prime")
else:
    while i < num:
        if num % i == 0:
            print("Not prime")
            break
        i += 1
    else:
        print("Prime")

# 2.sum of digits of given number
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10    
    sum += digit   
    num //= 10            

print("Sum of digits:", sum)

# 3.entered number is palindrome or not
n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4.reverse the given number
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reversed number:", rev)

# 1.print the multiplication table
n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

# 2.largest of n numbers
n = int(input("How many numbers? "))
i = 0
largest = None

while i < n:
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num
    i += 1

print("Largest:", largest)

# 3.smallest of n numbers
n = int(input("How many numbers? "))
i = 0
smallest = None

while i < n:
    num = int(input("Enter number: "))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print("Smallest:", smallest)


