import random
import argparse
import json
import os
import matplotlib.pyplot as plt
import numpy as np

class HoffmanGame:
    def __init__(self, dim=50, p_dense=0.02, k_birth=0.3, k_death=0.2, k_death_ai=0.2,
                 k_death_machine=0.1, k_aicreate=0.0003, k_compcreate=0.00005):
        self.dim = dim
        self.p_dense = p_dense
        self.k_birth = k_birth
        self.k_death = k_death
        self.k_deathai = k_death_ai
        self.k_deathmachine = k_death_machine
        self.k_aicreate = k_aicreate
        self.k_compcreate = k_compcreate

        self.mat = [[0 for _ in range(dim)] for _ in range(dim)]
        self.P = [[0 for _ in range(dim)] for _ in range(dim)] # Probability of not moving
        self.agents = []
        
        self.c_man = 0
        self.c_machine = 0
        self.c_ai = 0
        
        self.history = {'time': [], 'humans': [], 'machines': [], 'ai': []}

    def _initialize_world(self):
        """Initializes the world with humans."""
        for i in range(self.dim):
            for j in range(self.dim):
                if random.uniform(0, 1) < self.p_dense:
                    self.mat[i][j] = 1 # 1 for human
                    self.P[i][j] = 1
                    self.agents.append((i, j))
                    self.c_man += 1

    def _move_agent(self, agent_idx):
        """Moves a single agent."""
        i, j = self.agents[agent_idx]
        moves = [
            ((i - 1) % self.dim, j), ((i + 1) % self.dim, j),
            (i, (j - 1) % self.dim), (i, (j + 1) % self.dim)
        ]
        random.shuffle(moves)
        for new_i, new_j in moves:
            if self.mat[new_i][new_j] == 0:
                self.mat[new_i][new_j] = self.mat[i][j]
                self.mat[i][j] = 0
                self.P[new_i][new_j] = self.P[i][j]
                self.P[i][j] = 0
                self.agents[agent_idx] = (new_i, new_j)
                break

    def run_simulation(self, time_steps=1000, birth_death_interval=100, save_interval=0, save_path="game_state.json", plot_output_path=None):
        """Runs the main simulation loop."""
        if not os.path.exists(save_path):
            self._initialize_world()
            print("Initialized new game world.")
        else:
            self.load_game(save_path)
            print("Loaded game state.")

        print("Starting simulation...")
        for t in range(time_steps):
            random.shuffle(self.agents)

            if t > 0 and t % birth_death_interval == 0:
                pass 

            for idx in range(len(self.agents)):
                self._move_agent(idx)

            # Record history
            self.history['time'].append(t)
            self.history['humans'].append(self.c_man)
            self.history['machines'].append(self.c_machine)
            self.history['ai'].append(self.c_ai)

            if (t + 1) % 100 == 0:
                print(f"Time: {t+1}, Humans: {self.c_man}, Machines: {self.c_machine}, AI: {self.c_ai}")
            
            if save_interval > 0 and (t + 1) % save_interval == 0:
                self.save_game(save_path)
                print(f"Game state saved at time {t+1} to {save_path}")

        print("Simulation finished.")
        if plot_output_path:
            self.plot_history(plot_output_path)

    def save_game(self, filepath):
        """Saves the current game state to a JSON file."""
        state = {
            'dim': self.dim,
            'p_dense': self.p_dense,
            'k_birth': self.k_birth,
            'k_death': self.k_death,
            'k_deathai': self.k_deathai,
            'k_deathmachine': self.k_deathmachine,
            'k_aicreate': self.k_aicreate,
            'k_compcreate': self.k_compcreate,
            'mat': self.mat,
            'P': self.P,
            'agents': self.agents,
            'c_man': self.c_man,
            'c_machine': self.c_machine,
            'c_ai': self.c_ai,
            'history': self.history, # Save history as well
        }
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=4)

    def load_game(self, filepath):
        """Loads the game state from a JSON file."""
        with open(filepath, 'r') as f:
            state = json.load(f)
        
        self.dim = state['dim']
        self.p_dense = state['p_dense']
        self.k_birth = state['k_birth']
        self.k_death = state['k_death']
        self.k_deathai = state['k_deathai']
        self.k_deathmachine = state['k_deathmachine']
        self.k_aicreate = state['k_aicreate']
        self.k_compcreate = state['k_compcreate']
        self.mat = state['mat']
        self.P = state['P']
        self.agents = [tuple(a) for a in state['agents']]
        self.c_man = state['c_man']
        self.c_machine = state['c_machine']
        self.c_ai = state['c_ai']
        self.history = state.get('history', {'time': [], 'humans': [], 'machines': [], 'ai': []}) # Load history
    
    def plot_history(self, output_path="simulation_history.png"):
        """Plots the population history of humans, machines, and AI."""
        print(f"Generating plot to {output_path}...")
        plt.figure(figsize=(10, 6))
        plt.plot(self.history['time'], self.history['humans'], label='Humans')
        plt.plot(self.history['time'], self.history['machines'], label='Machines')
        plt.plot(self.history['time'], self.history['ai'], label='AI')
        plt.xlabel('Time Steps')
        plt.ylabel('Population Count')
        plt.title('Hoffman Game Simulation History')
        plt.legend()
        plt.grid(True)
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Hoffman Game simulation.")
    parser.add_argument('--dim', type=int, default=50, help="Dimension of the simulation grid.")
    parser.add_argument('--steps', type=int, default=1000, help="Number of time steps to run.")
    parser.add_argument('--density', type=float, default=0.02, help="Initial density of humans.")
    parser.add_argument('--save_interval', type=int, default=100, help="Interval to save game state (0 for no saving).")
    parser.add_argument('--save_path', type=str, default="game_state.json", help="Path to save/load game state.")
    parser.add_argument('--plot_path', type=str, default="simulation_history.png", help="Path to save the simulation history plot.")

    args = parser.parse_args()

    game = HoffmanGame(dim=args.dim, p_dense=args.density)
    game.run_simulation(time_steps=args.steps, save_interval=args.save_interval, 
                         save_path=args.save_path, plot_output_path=args.plot_path)