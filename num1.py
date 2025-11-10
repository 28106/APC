import numpy as np
a = np.array([10, 5, 6, 9, 2])
b = np.array([7, 1, 5, 3, 11])

print("Arary A :",a)
print("Array B:", b)

add = np.add(a, b)
print("\nAddition of A & B is:", add)


mul= np.multiply(a, b)
print("\nMutiplication of A & B is:", mul)

sub = np.subtract(a, b)
print("\nAddition of A & B is:", sub)


div= np.divide(a, b)

print("\nDivision of A & B is:", div)


mean_a = np.mean(a)
median_a = np.median(a)
print("\nMean of Array A:", mean_a)
print("\nMedian of Array A:",median_a)

print("\nMinimum Value of A:", np.min(a))
