square = lambda x: x * x
print(square(5))  


add = lambda a, b: a + b
print(add(10, 20))


print((lambda x, y: x * y)(4, 5))  


nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, nums))
print(squares)  


nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  


