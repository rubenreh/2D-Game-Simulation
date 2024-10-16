# 2D-Game Simulation
# Author : Ruben Rehal
# Date : July 14, 2024

import numpy as np
from particle import Particle

def initialize_particles(num_particles, grid_size):
    """
    Initializes particles with random positions and velocities.

    :param num_particles: Number of particles to initialize (int).
    :param grid_size: Size of the grid (int).
    :return: List of initialized Particle objects.
    """
    particles = []
    for _ in range(num_particles):
        position = np.random.rand(2) * grid_size  # Random position
        velocity = (np.random.rand(2) - 0.5) * 2   # Random velocity
        particles.append(Particle(position, velocity))
    return particles
