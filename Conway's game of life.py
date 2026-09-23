import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Game of Life implementation
N = 100
grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)

def update(frameNum, img, grid, N): 
    newGrid = grid.copy()
    for i in range(N): 
        for j in range(N): 
            # Count neighbors using toroidal boundary conditions
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
                         
            # Apply Conway's Game of Life rules
            if grid[i, j] == 1: 
                if (total < 2) or (total > 3): 
                    newGrid[i, j] = 0
            else: 
                if total == 3: 
                    newGrid[i, j] = 1
    
    # Update the image and grid
    img.set_data(newGrid)
    grid[:] = newGrid[:]  # Update original grid
    return img,

# Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), 
                            frames=100, interval=50, blit=True)

# Display the animation
plt.show()  # Fixed: added parentheses to actually call the function
