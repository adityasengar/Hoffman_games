# Hoffman_games

# Reinforcement Learning Simulation of Human, Robot, and AI Interaction

This simulation models the interactions between Humans, Robots, and AIs in a 2D grid world using Q-learning, a type of Reinforcement Learning algorithm. There are two Humans and two Robots initially present. Special events occur when certain entities encounter each other:

- When a Human and a Robot meet, they form an AI entity with a high reward.
- When two Humans meet, the reward for forming an AI decreases.
- When two Robots meet, no special event occurs.

## Dependencies

This project requires Python 3 and NumPy. If you don't have Python 3 installed, download it from the [official Python website](https://www.python.org/). To install NumPy, you can use pip:



## Running the Simulation

To run the simulation, simply navigate to the directory containing the Python file in your terminal and run the following command:



Replace "Hoffman_RL.py" with the name of the Python file.

## Simulation Details

The simulation is conducted in episodes. In each episode, Humans and Robots are placed randomly in the world. They then move around the world according to the Q-learning policy.

The world is a 2D grid of size 5x5. The available actions are: Up, Down, Left, and Right. Entities cannot move outside the boundaries of the world.

Rewards in the simulation are as follows:
- Forming an AI (when a Human and Robot meet): 100 points
- Forming an AI after two Humans have met: 50 points
- Each move: -1 point

The simulation uses the following Q-learning hyperparameters:
- Learning rate (Alpha): 0.5
- Discount factor (Gamma): 0.9
- Epsilon for Epsilon-Greedy policy: 0.1
- Number of episodes: 5000

## Output

The simulation will output the Q-tables for the two Humans and two Robots. These tables represent the learned policy for each entity and indicate the action (Up, Down, Left, Right) that the entity will choose in each state (grid cell).
