import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)
#set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
#set size of a tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
