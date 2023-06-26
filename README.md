# Hoffman_games

# Reinforcement Learning Simulation of Human, Robot, and AI Interaction

This simulation models the interactions between Humans, Robots, and AIs in a 2D grid world. There are Humans and Machines initially present. Special events occur when certain entities encounter each other:

- Humans have a natural birth rate (by reproduction), and a natural death rate.
- Machines have a natural death rate smaller than the death rate of humans. 
- Machines are also depleted when AI is formed.
- AI has a natural death rate that is smaller than the death rate of humans.
- At time t=0, the world consists of only humans. 
- A human can move left, right, up, down or stay where they are.
- If a human sees another human nearby, the tendency of both humans to stay at their respective location increases. This condition resembles a process of cooperation between human beings to ensure maximal survival.
- Whenever 2 humans are nearby, they have a chance to construct a machine which is placed randomly in the near vicinity of the human pair.
- If a human sees a machine nearby, it has a chance to fuse with the machine to become AI.

## Dependencies

This project requires Python 3 and NumPy, random and math libraries. If you don't have Python 3 installed, download it from the [official Python website](https://www.python.org/). To install NumPy, you can use pip:



## Running the Simulation

To run the simulation, simply navigate to the directory containing the Python file in your terminal and run the following command:

Replace "Hoffman_games.py" with the name of the Python file.

## Output

The simulation will output 2 files:
- matrix_vs_t.dat: The 50x50 matrix (in default case) containing positions of human, machines, AI output after every 10 time steps
- density_vs_t.dat: Density of human, machine, AI vs time 


# Analysis.nb

This file is used to analyse the 2 output files, create movies and make plots
