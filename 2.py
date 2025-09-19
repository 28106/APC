# 1. check number is zero or non zero value
n = int(input("Enter any number:"))
if n==0:
    print("Number is zero")
else:
    print("non zero value")

# 2.largest of two number
a=int(input("Enter first number"))

b=int(input("Enter second number"))
if a>b:
    print("A is greater",a)
else:
    print("B is Greater",b)

# 3.check the number is positive or negative
n = int(input("Enter any number:/n"))  

if n > 0:
    print("Number is Positive")
elif n < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# 4.check entered character is vowel or consonant 
str = (input("Enter any character:"))
if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str =='u':
    print(str,"It is vowel")
else:
    print(str,"It is Consonant")

# 1.student performance
per = int(input("Enter percentage:"))
if per>= 90:
    print("Excellenrt Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print(" Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")

# 2.largest of three numbers
a = int(input("Enter first number:/n"))
b = int(input("Enter second number:/n"))
c = int(input("Enter third number:/n"))

if a>b and a>c:
    print ("A is Greater")
elif b>a and b>c:
    print("B is Greater")
else:
    print("C is Greater")



# 3.smallest of three numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a<b and a<c:
    print ("A is Smaller")
elif b<a and b<c:
    print("B is Smaller")
else:
    print("C is Smaller")

# 1.natural numbers upto n
n = int(input("Enter any number:"))
count = 1
while count<n:
    print(count)
    count += 1

# 2.even numbers upto n
n = int(input("Enter any number:"))
count = 1
while count<n:
    if n%2==0:
        print(count)
    count += 1

# 3.odd numbers upto n
n = int(input("Enter any number:"))
for i in range (1, n, 2):
    print(i)

# 4.sum of natural number upto n
n = int(input("Enter any number: "))
total = 0
for i in range(1, n):
    total += i
print("Sum:", total)

# 1.sum of odd numbers upto n
n = int(input("Enter any number: "))
total = 0
for i in range(1, n, 2):
    total += i
print("Sum:", total)

# 2.sum of even number upto n
n = int(input("Enter any number: "))
total = 0
for i in range(2, n, 2):
    print(i)
    total += i
print("Sum:", total)

# 3.natural numbers upto n in reverse order
n = int(input("Enter any number: "))
for i in range(n, 0, -1):
    print(i)

# 4.fibonacci series upto n
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1

# 5.factorial of given number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)


















