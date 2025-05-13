# **Water Sort Puzzle Solver**

This project provides a Python implementation of a **Water Sort Puzzle Solver** using the A* algorithm. It includes functionality to generate random initial configurations for the puzzle and solve them step-by-step.

---

## **Overview**

The Water Sort Puzzle is a sorting game where liquids of different colors are mixed in multiple tubes. The goal is to sort the colors so each tube contains a single color or is completely empty.

This project includes:
1. **`solver.py`**: Solves a given Water Sort Puzzle using the A* search algorithm.
2. **`generate_initial_tubes.py`**: Generates a random initial configuration for the puzzle with customizable parameters.

---

## **Features**

- **Puzzle Generator**:
  - Randomly generate an initial configuration of tubes with specified colors, tube count, and capacity.
- **Puzzle Solver**:
  - Solves the puzzle using the A* algorithm, which finds the optimal solution path.
  - Heuristic-based cost function to prioritize moves efficiently.
- **Step-by-Step Solution**:
  - Displays the solution path with detailed steps.

---

## **Requirements**

- Python 3.7 or higher

---

## **Setup**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/angus4718/water_sort.git
   cd water_sort
   ```

2. **Install Dependencies** (if any):
   - The project uses only the Python standard library, so no additional dependencies are required.

---

## **Usage**

### **1. Generate Initial Puzzle Configuration**

You can use `generate_initial_tubes.py` to create a random puzzle configuration.

Run the script:
```bash
python generate_initial_tubes.py
```

Customize the number of tubes, colors, and tube capacity:
```python
num_tubes = 10       # Total tubes (including empty)
num_colors = 8       # Number of colors
tube_capacity = 4    # Capacity of each tube
```

**Example Output**:
```plaintext
initial_tubes = [
    ['A', 'B', 'C', 'D'],
    ['D', 'C', 'B', 'A'],
    ['A', 'A', 'B', 'B'],
    ['C', 'D', 'D', 'C'],
    ['', '', '', ''],
    ['', '', '', ''],
]
```

---

### **2. Solve the Puzzle**

Use `solver.py` to solve a given puzzle configuration.

Edit the `initial_tubes` variable in `solver.py` to include your puzzle configuration:
```python
initial_tubes = [
    ['A', 'B', 'C', 'D'],
    ['D', 'C', 'B', 'A'],
    ['A', 'A', 'B', 'B'],
    ['C', 'D', 'D', 'C'],
    ['', '', '', ''],
    ['', '', '', ''],
]
```

Run the solver:
```bash
python solver.py
```

**Example Output**:
```plaintext
Current State: [['A', 'B', 'C', 'D'], ['D', 'C', 'B', 'A'], ...], Cost: 0, Path: []
Valid Moves: [(0, 4), (1, 5), ...]
Applying Move: (0, 4)
Resulting State: [['A', 'B', 'C', ''], ['D', 'C', 'B', 'A'], ...]

Solution found!
Step 1: Move from tube 1 to tube 5
Step 2: Move from tube 2 to tube 6
...
```

---

## **Code Structure**

### **1. `generate_initial_tubes.py`**

- **Purpose**: Generates a random puzzle configuration.
- **Function**:
  ```python
  generate_initial_tubes(num_tubes: int, num_colors: int, tube_capacity: int) -> List[List[str]]
  ```
  - Generates a list of tubes with randomly distributed colors.

### **2. `solver.py`**

- **Purpose**: Solves the Water Sort Puzzle using the A* algorithm.
- **Key Components**:
  - **`WaterSortPuzzle` class**:
    - Represents the puzzle and handles moves, undoing moves, and heuristic calculations.
  - **`a_star_solver` function**:
    - Implements the A* algorithm to find the optimal solution.

---

## **Customization**

- Modify the number of tubes, colors, and capacity in `generate_initial_tubes.py`.
- Replace the `initial_tubes` in `solver.py` with custom configurations.

---

## **Contributing**

Feel free to submit pull requests or report issues to improve the project.

---

## **License**

This project is licensed under the MIT License.