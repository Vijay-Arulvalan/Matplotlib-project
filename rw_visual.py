import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make a random walk and plot the points
rw = RandomWalk() #we create a random walk and store it in rw
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values,c='Red', edgecolor='none', s=10) #c=rw.y_values, cmap=plt.cm.Reds
plt.savefig('rw.png', bbox_inches='tight')
plt.show()
