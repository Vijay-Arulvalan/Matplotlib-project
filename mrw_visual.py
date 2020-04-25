#multiple random walk and styling
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    mrw = RandomWalk(50000) #we create a random walk and store it in rw
    mrw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6)) #it control width, height, background, resolution
    point_number = list(range(mrw.num_points))
    plt.scatter(mrw.x_values, mrw.y_values,c=point_number, cmap=plt.cm.Reds, edgecolor='none', s=10)
    #Emphasis the first and last points
    plt.scatter(0, 0, c='green', edgecolor='none', s=100) #starting point in Green
    plt.scatter(mrw.x_values[-1], mrw.y_values[-1], c='red', edgecolors='none', s=100) #ending point in Red
    plt.savefig('mrw.png', bbox_inches='tight')
    plt.show()

    keep_running = input("Make Another walk (Y/N): ")
    if keep_running == 'n':
        break
