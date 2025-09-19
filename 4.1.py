# 1.print the natural numbers upto n
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)

# 2.print even numbers upto n
n = int(input("Enter a number: "))

for i in range(2, n + 1, 2):
    print(i)

# 3.print odd numbers upto n
n = int(input("Enter a number: "))

for i in range(1, n + 1, 2):
    print(i)

# 4.print 1 2 4 8 16 32 ... n^2
n = int(input("Enter a number: "))
val = 1

for _ in range(n):
    print(val, end=" ")
    val *= 2

# 5.sum the given sequence 1+1/1!+1/2!+1/3!+...+1/n!
n = int(input("Enter n:"))
fact = 1
total = 1
for i in range(1, n+1):
    fact *= i
    total += 1/fact
print("Sum :", total)

# 6.compute the cosine series
import math

x = float(input("Enter value of x in degrees: "))
n = int(input("Enter number of terms: "))

x = math.radians(x)

cos_x = 0
sign = 1
fact = 1

for i in range(n):
    power = 2 * i
    if power > 0:
        fact = 1
        for j in range(1, power + 1):
            fact *= j
    cos_x += sign * (x ** power) / fact
    sign *= -1

print("Cos(x) =", cos_x)

# 7.check weather the square root of number is prime or not 
import math

n = int(input("Enter a number: "))
root = int(math.sqrt(n))

if root * root != n:
    print("Square root is not an integer.")
else:
    if root > 1:
        for i in range(2, root):
            if root % i == 0:
                print("Square root is not prime.")
                break
        else:
            print("Square root is prime.")
    else:
        print("Square root is not prime.")

# 8.A B C
#   A B C
#   A B C
for i in range(3):         
    for j in range(65, 68):  
        print(chr(j), end=" ")
    print()

# 9.A
#   A B
#   A B C
#   A B C D
#   A B C D E
n = int(input("Enter value: "))

for i in range(1, n + 1):
    for j in range(65, 65 + i):  # ASCII for 'A' is 65
        print(chr(j), end=" ")
    print()

# 10.A B C D E
#    A B C D
#    A B C
#    A B
#    A
n = int(input("Enter value: "))

for i in range(n, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()

# 11.1
#    1 2
#    1 2 3 
#    1 2 3 4 
#    1 2 3 4 5 
n = int(input("Enter value: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 12.1
#    2 2 
#    3 3 3 
#    4 4 4 4
#    5 5 5 5 5 
n = int(input("Enter value: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

   