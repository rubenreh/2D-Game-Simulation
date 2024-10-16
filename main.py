# 2D-Game Simulation
# Author : Ruben Rehal
# Date : July 14, 2024

import numpy as np
import matplotlib.pyplot as plt
from particle import Particle
from grid import Grid
from utils import initialize_particles

# Constants
GRID_SIZE = 50       # Size of the grid (50x50)
NUM_PARTICLES = 100  # Number of particles
STEPS = 100          # Number of simulation steps

def main():
    # Initialize grid and particles
    grid = Grid(GRID_SIZE)
    particles = initialize_particles(NUM_PARTICLES, GRID_SIZE)

    # Run the simulation for a number of steps
    for step in range(STEPS):
        grid.update(particles)  # Update particle positions
        grid.display(step)       # Display the grid

    plt.show()  # Show the final plot

if __name__ == "__main__":
    main()
