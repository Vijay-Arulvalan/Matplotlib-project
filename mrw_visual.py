#multiple random walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    mrw = RandomWalk() #we create a random walk and store it in rw
    mrw.fill_walk()

    plt.scatter(mrw.x_values, mrw.y_values,c='Blue', edgecolor='none', s=10) #c=rw.y_values, cmap=plt.cm.Reds
    plt.savefig('mrw.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make Another walk (Y/N): ")
    if keep_running == 'n':
        break
