import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

size = 100 
p = 0.05   
f = 0.001  
density = 0.5

EMPTY, TREE, FIRE, BURNT = 0, 1, 2, 3

forest = np.random.choice([EMPTY, TREE], size=(size, size), p=[1-density, density])

def step(forest):
    new_forest = forest.copy()
    for i in range(size):
        for j in range(size):
            if forest[i, j] == EMPTY or forest[i, j] == BURNT:
                if np.random.rand() < p:
                    new_forest[i, j] = TREE
            elif forest[i, j] == TREE:
                neighbors = [
                    forest[(i-1)%size, j],
                    forest[(i+1)%size, j],
                    forest[i, (j-1)%size],
                    forest[i, (j+1)%size]
                ]
                if FIRE in neighbors:
                    new_forest[i, j] = FIRE
                elif np.random.rand() < f:
                    new_forest[i, j] = FIRE
            elif forest[i, j] == FIRE:
                new_forest[i, j] = BURNT
    return new_forest

cmap = plt.cm.get_cmap('YlGnBu', 4)
fig, ax = plt.subplots()
im = ax.imshow(forest, cmap=cmap, vmin=0, vmax=3)

def update(*args):
    global forest
    forest = step(forest)
    im.set_array(forest)
    return [im]

ani = animation.FuncAnimation(fig, update, interval=50, blit=True)
plt.show()
