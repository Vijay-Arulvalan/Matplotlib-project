import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values] #here we square a number and store it in y_values

plt.scatter(x_values, y_values, c=(0, 0.5, 0.5), edgecolor='none', s = 5) #we pass all the x and y values
# edgecolor used to solid points and c is a color we can use #to define color in RGB color module 3 decimal points one for red and one for green and one for blue
#using values between 0 and 1, values closer to 0 produce dark color and values closer to 1 produce light colors
plt.title("Square Numbers", fontsize=22)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
#plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 1100, 0, 1100000])

plt.show()
