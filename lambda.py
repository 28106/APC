square = lambda x: x * x
print(square(5))   # 25


add = lambda a, b: a + b
print(add(10, 20))  # 30


print((lambda x, y: x * y)(4, 5))  # 20


nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, nums))
print(squares)   # [1, 4, 9, 16, 25]


nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [10, 20, 30]


