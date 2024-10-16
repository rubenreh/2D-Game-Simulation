# 2D Game Simulation

## Project Overview

The **2D Game Simulation** project is a visual simulation that models the behavior of particles moving within a bounded grid. Utilizing object-oriented programming principles, each particle is represented as an individual object with attributes for position and velocity. This project serves as a practical demonstration of basic physics concepts, including particle dynamics, movement, and collision detection with grid boundaries. By visualizing particle interactions, the simulation provides insight into how systems of particles behave over time.

## How It Works

### Particle Initialization
- Each particle is initialized with a random position within the confines of the grid and a random velocity vector. The velocity determines the direction and speed at which the particle moves across the grid.
- The initialization process is handled in a dedicated utility function, which generates a specified number of particles based on user-defined parameters.

### Particle Movement
- At every simulation step, each particle updates its position based on its current velocity. The new position is calculated by adding the velocity vector to the current position.
- To ensure that particles remain within the boundaries of the grid, collision detection is implemented. If a particle reaches the edge of the grid, its velocity is reversed, simulating a bouncing effect. This behavior mimics real-world physics, where particles cannot pass through walls.

### Grid Management
- The `Grid` class acts as the primary container for the particles, providing methods to manage their positions and facilitate interactions between them.
- The grid is visualized using Matplotlib, where each particle's current position is represented as a point in a 2D space. The grid size can be easily modified to explore how the system behaves under different constraints.

### Visualization
- The simulation utilizes Matplotlib for dynamic visualization, allowing users to see the movement of particles in real time. The particles are displayed as blue dots, and the plot updates continuously during the simulation.
- The grid's limits are set to match the defined size, ensuring a clear representation of the simulation environment. As the simulation progresses, the plot refreshes at each step, creating an animated effect that makes the particle interactions more engaging.

### Future Enhancements
- This project provides a foundational understanding of basic physics simulations. There is ample opportunity for further development, including:
  - Implementing particle interactions, such as attraction or repulsion between particles.
  - Allowing variable velocities or adding forces to change particle dynamics.
  - Introducing new particle types with different behaviors or properties.
  - Enhancing the user interface for improved interaction with simulation parameters.

By expanding on the basic framework, the simulation can evolve into a more complex and informative model of particle behavior, offering deeper insights into physical systems.
