import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self, size):
        """
        Initializes the grid with a specified size.

        :param size: Size of the grid (int).
        """
        self.size = size  # Size of the grid

    def update(self, particles):
        """
        Updates the position of all particles.

        :param particles: List of Particle objects.
        """
        for particle in particles:
            particle.move(self.size)  # Move each particle

    def display(self, step):
        """
        Displays the grid with particles' current positions.

        :param step: Current simulation step (int).
        """
        plt.clf()  # Clear the current figure
        plt.title(f'Step {step}')
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        plt.gca().set_aspect('equal', adjustable='box')  # Equal aspect ratio

        # Plot each particle
        for particle in particles:
            plt.scatter(particle.position[0], particle.position[1], color='blue', s=10)
        plt.pause(0.1)  # Pause to create an animation effect
