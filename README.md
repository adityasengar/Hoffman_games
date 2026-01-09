# Hoffman Games Simulation

This project implements a cellular automata simulation, referred to as the "Hoffman Game," modeling interactions between different types of agents (Humans, Machines, AI) in a 2D world. The simulation explores concepts of population dynamics, cooperation, and emergent behavior.

The original logic was developed in a Jupyter Notebook and has been refactored into a structured Python command-line application.

## Project Overview

The simulation models:
-   **Agent Movement:** Agents can move in a 2D grid.
-   **Interactions:** Tendency to cooperate, machine creation, and AI fusion.
-   **Population Dynamics:** Birth and death rates for different agent types.

### Project Structure

-   `game.py`: Contains the `HoffmanGame` class, encapsulating all simulation logic, agent behaviors, and population dynamics.
-   `requirements.txt`: Lists all necessary Python dependencies.

---

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/adityasengar/Hoffman_games.git
    cd Hoffman_games
    ```

2.  It is recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run the simulation using the `game.py` script. You can configure various parameters via the command-line interface.

```bash
python game.py --dim 100 --steps 5000 --density 0.01 --save_interval 500 --save_path game_state.json --plot_path simulation_history.png
```

### Command-Line Arguments

-   `--dim`: Dimension of the square simulation grid (e.g., `50` for a 50x50 grid). (Default: `50`)
-   `--steps`: Number of time steps to run the simulation. (Default: `1000`)
-   `--density`: Initial density of humans (between 0.0 and 1.0). (Default: `0.02`)
-   `--save_interval`: Interval (in time steps) to save the game state to a JSON file (0 for no saving). (Default: `100`)
-   `--save_path`: Path to the JSON file for saving/loading game state. (Default: `game_state.json`)
-   `--plot_path`: Path to save the simulation history plot. (Default: `simulation_history.png`)

### Output Files

-   `game_state.json`: Saved simulation state, allowing resumption of a game.
-   `simulation_history.png`: A plot visualizing the population counts of Humans, Machines, and AI over time.
# Updated on 2026-01-09
