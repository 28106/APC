# Creating from a list
fs1 = frozenset([1, 2, 3, 4])
print(fs1)   

# Creating from a string
fs2 = frozenset("hello")
print(fs2)   


fs = frozenset([10, 20, 30, 40])



print(20 in fs)   
print(len(fs))    


A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A | B)   
print(A & B)   
print(A - B)   
print(A ^ B)


cities = {
    frozenset(["Pune", "Mumbai"]): "Maharashtra",
    frozenset(["Delhi", "Noida"]): "NCR"
}

print(cities[frozenset(["Pune", "Mumbai"])])  


