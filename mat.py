import matplotlib.pyplot as plt
import numpy as np
# Bar
subject = ['Math', 'Science','English','History','Computer']
marks = [85, 90, 78, 88, 95] 

plt.figure(figsize = (10, 6))
plt.bar(subject, marks,color = 'pink', edgecolor='black')
plt.title("Bar Chart Representation")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(axis = 'y', linestyle = '--', alpha=0.7)
plt.show();




# Histogram
ages = np.random.randint(18, 50, 100)
plt.figure(figsize= (10, 6))
plt.hist(ages, color = 'lightgreen',edgecolor = 'black')
plt.title("Histrogram Representation")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis= 'y', linestyle='-', alpha=0.7)
plt.show()



# Scatter
x = np.random.randint(1, 50, 30)
y = np.random.randint(1, 50, 30)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', s=80, edgecolors='black')
plt.title("Scatter plot presentation")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True, linestyle='--',alpha = 0.6)
plt.show()



#Line Graph
months = ['Jan','Feb','Mar','Apr','May','Jun']
sales = [120, 50, 180, 20, 260, 30]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker = 'o', color='purple', linewidth = 2)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True,linestyle = '--', alpha=0.6)
plt.show()