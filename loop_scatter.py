import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values] #here we square a number and store it in y_values

plt.scatter(x_values, y_values, c='cyan', edgecolor='none', s = 5) #we pass all the x and y values
# edgecolor used to solid points and c is a color we can use
plt.title("Square Numbers", fontsize=22)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
#plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 1100, 0, 1100000])

plt.show()
