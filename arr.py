import array


arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)     


arr = array.array('i', [10, 20, 30, 40, 50])

print(arr[0])    
print(arr[-1]) 
print(arr[1:4]) 



arr = array.array('i', [1, 2, 3])

arr.append(4)       
arr.insert(1, 10)    
arr.extend([20, 30])  

print(arr)  


arr = array.array('i', [1, 2, 3, 4, 5])

arr.remove(3)    
arr.pop()       
del arr[0]       

print(arr)   


arr = array.array('i', [10, 20, 30, 40])

for x in arr:
    print(x)


arr = array.array('i', [5, 2, 8, 1, 9])

print(len(arr))      
print(min(arr))      
print(max(arr))      
print(sum(arr))       


