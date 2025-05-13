import random
from typing import List

def generate_initial_tubes(num_tubes: int, num_colors: int, tube_capacity: int) -> List[List[str]]:
    """
    Generate an initial configuration for the Water Sort Puzzle.

    Args:
        num_tubes (int): Total number of tubes (including empty ones).
        num_colors (int): Total number of colors.
        tube_capacity (int): Capacity of each tube.

    Returns:
        list: A list of lists representing the tubes.
    """
    colors = [chr(65 + i) for i in range(num_colors)]  # A, B, C, ..., etc.
    color_pool = colors * tube_capacity  # Repeat each color exactly tube_capacity times

    random.shuffle(color_pool)

    tubes = [color_pool[i * tube_capacity:(i + 1) * tube_capacity] for i in range(num_colors)]

    for _ in range(num_tubes - num_colors):
        tubes.append([''] * tube_capacity)

    random.shuffle(tubes)

    return tubes


if __name__ == "__main__":
    num_tubes = 10       # Total tubes (including empty)
    num_colors = 8      # Number of colors
    tube_capacity = 4   # Capacity of each tube

    initial_tubes = generate_initial_tubes(num_tubes, num_colors, tube_capacity)

    print("initial_tubes = [")
    for tube in initial_tubes:
        print(f"    {tube},")
    print("]")