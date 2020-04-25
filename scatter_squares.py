import matplotlib.pyplot as plt
# scatter means individual points, we can customize that with colors and size or anything, we can customize every single point in the plot
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, edgecolor='none', s=40)
#set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
#set size of a tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
