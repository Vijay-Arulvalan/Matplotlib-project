import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=2) #line linewidth controls the thickness of the line
#set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of label", fontsize=14)
#set size of tick label
plt.tick_params(axis ='both', labelsize=14)

plt.show()
