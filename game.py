import random
import argparse

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

    def run_simulation(self, time_steps=1000, birth_death_interval=100):
        """Runs the main simulation loop."""
        self._initialize_world()
        
        print("Starting simulation...")
        for t in range(time_steps):
            random.shuffle(self.agents)

            if t > 0 and t % birth_death_interval == 0:
                pass # Placeholder for birth/death logic

            for idx in range(len(self.agents)):
                self._move_agent(idx)

            if (t + 1) % 100 == 0:
                print(f"Time: {t+1}, Humans: {self.c_man}, Machines: {self.c_machine}, AI: {self.c_ai}")
        
        print("Simulation finished.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Hoffman Game simulation.")
    parser.add_argument('--dim', type=int, default=50, help="Dimension of the simulation grid.")
    parser.add_argument('--steps', type=int, default=1000, help="Number of time steps to run.")
    parser.add_argument('--density', type=float, default=0.02, help="Initial density of humans.")
    args = parser.parse_args()

    game = HoffmanGame(dim=args.dim, p_dense=args.density)
    game.run_simulation(time_steps=args.steps)