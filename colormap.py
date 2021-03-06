import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s = 20) #we need add s in all colors we need for example Blues, Reds
plt.title("Square Numbers", fontsize=22)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
#plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 1100, 0, 1100000])

plt.savefig('color.png', bbox_inches='tight') #to save in png we need to use this command
#the second argument bbox_inches trims extra whitespace from the plot
plt.show()
