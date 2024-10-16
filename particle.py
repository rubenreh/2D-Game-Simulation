# 2D-Game Simulation
# Author : Ruben Rehal
# Date : July 14, 2024

import numpy as np

class Particle:
    def __init__(self, position, velocity):
        """
        Initializes a Particle object with a given position and velocity.

        :param position: Initial position of the particle (numpy array).
        :param velocity: Velocity of the particle (numpy array).
        """
        self.position = position  # Current position of the particle
        self.velocity = velocity    # Current velocity of the particle

    def move(self, grid_size):
        """
        Updates the position of the particle based on its velocity.
        Ensures the particle bounces off the walls of the grid.

        :param grid_size: Size of the grid (int).
        """
        # Update position
        self.position += self.velocity

        # Bounce off the walls
        for i in range(2):
            if self.position[i] < 0 or self.position[i] >= grid_size:
                self.velocity[i] *= -1  # Reverse direction
                self.position[i] = np.clip(self.position[i], 0, grid_size - 1)  # Keep within bounds
