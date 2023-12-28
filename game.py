import random
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
        
        # Simplified movement logic from notebook
        moves = [
            ((i - 1) % self.dim, j), # Up
            ((i + 1) % self.dim, j), # Down
            (i, (j - 1) % self.dim), # Left
            (i, (j + 1) % self.dim)  # Right
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

    def run_simulation(self, time_steps=1000, birth_death_interval=100):
        """Runs the main simulation loop."""
        self._initialize_world()
        
        print("Starting simulation...")
        for t in range(time_steps):
            random.shuffle(self.agents)

            # Simplified logic from notebook
            if t % birth_death_interval == 0 and t > 0:
                # Placeholder for birth/death logic
                pass

            for idx in range(len(self.agents)):
                self._move_agent(idx)
                # Placeholder for neighbor interactions, AI creation etc.

            if (t + 1) % 100 == 0:
                print(f"Time: {t+1}, Humans: {self.c_man}, Machines: {self.c_machine}, AI: {self.c_ai}")
        
        print("Simulation finished.")


if __name__ == '__main__':
    game = HoffmanGame()
    game.run_simulation()
