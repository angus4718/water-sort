import copy
import heapq
from typing import List, Tuple, Optional

class WaterSortPuzzle:
    def __init__(self, tubes: List[List[str]]):
        """
        Initialize the puzzle with the given tubes.

        Args:
            tubes (list): A list of lists representing the tubes. Each sublist contains strings for colors or '' for empty spaces.
        """
        self.tubes = tubes
        self.num_tubes = len(tubes)
        self.tube_capacity = len(tubes[0])

    def is_solved(self) -> bool:
        """
        Check if the puzzle is solved.

        Returns:
            bool: True if all tubes are either empty or contain only one color, False otherwise.
        """
        for tube in self.tubes:
            if len(set(tube)) > 1:
                return False
        return True

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        """
        Generate all valid moves as (from_tube, to_tube) pairs.

        Returns:
            list: A list of tuples representing valid moves. Each tuple is (from_tube, to_tube).
        """
        moves = []
        for from_tube in range(self.num_tubes):
            if not any(color != '' for color in self.tubes[from_tube]):
                continue

            from_color = None
            for color in reversed(self.tubes[from_tube]):
                if color != '':
                    from_color = color
                    break

            for to_tube in range(self.num_tubes):
                if from_tube == to_tube:
                    continue

                if not any(color != '' for color in self.tubes[to_tube]):
                    moves.append((from_tube, to_tube))
                    continue

                to_color = None
                for color in reversed(self.tubes[to_tube]):
                    if color != '':
                        to_color = color
                        break

                if to_color == from_color and self.tubes[to_tube].count('') > 0:
                    moves.append((from_tube, to_tube))

        return moves

    def apply_move(self, move: Tuple[int, int]) -> None:
        """
        Apply a move to the puzzle.

        Args:
            move (tuple): A tuple (from_tube, to_tube) representing the move to apply.
        """
        from_tube, to_tube = move

        from_color = None
        num_to_move = 0

        for i in range(len(self.tubes[from_tube]) - 1, -1, -1):
            if self.tubes[from_tube][i] != '':
                if from_color is None:
                    from_color = self.tubes[from_tube][i]
                    num_to_move = 1
                elif self.tubes[from_tube][i] == from_color:
                    num_to_move += 1
                else:
                    break

        empty_slots = self.tubes[to_tube].count('')

        num_to_move = min(num_to_move, empty_slots)

        for _ in range(num_to_move):
            for i in range(len(self.tubes[from_tube]) - 1, -1, -1):
                if self.tubes[from_tube][i] != '':
                    color = self.tubes[from_tube][i]
                    self.tubes[from_tube][i] = ''
                    break

            for i in range(len(self.tubes[to_tube])):
                if self.tubes[to_tube][i] == '':
                    self.tubes[to_tube][i] = color
                    break

    def undo_move(self, move: Tuple[int, int], color: str) -> None:
        """
        Undo a move and restore the tube states.

        Args:
            move (tuple): A tuple (from_tube, to_tube) representing the move to undo.
            color (str): The color being moved back.
        """
        from_tube, to_tube = move

        for i in range(len(self.tubes[to_tube]) - 1, -1, -1):
            if self.tubes[to_tube][i] != '':
                self.tubes[to_tube][i] = ''
                break

        for i in range(len(self.tubes[from_tube])):
            if self.tubes[from_tube][i] == '':
                self.tubes[from_tube][i] = color
                break

    def heuristic(self) -> int:
        """
        Calculate the heuristic cost of the current puzzle state.

        Returns:
            int: The heuristic cost based on the number of mixed colors and empty spaces in unsolved tubes.
        """
        cost = 0
        for tube in self.tubes:
            unique_colors = set([color for color in tube if color != ''])
            if len(unique_colors) > 1:
                cost += len(unique_colors) - 1
            if '' in tube and len(unique_colors) > 0:
                cost += tube.count('')
        return cost


def a_star_solver(puzzle: WaterSortPuzzle) -> Optional[List[Tuple[int, int]]]:
    """
    Solve the Water Sort Puzzle using the A* algorithm.

    Args:
        puzzle (WaterSortPuzzle): The puzzle instance to solve.

    Returns:
        list: A list of moves (from_tube, to_tube) representing the solution path, or None if no solution exists.
    """
    initial_state = copy.deepcopy(puzzle.tubes)
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, initial_state, []))
    visited_states = set()

    while priority_queue:
        _, cost, current_state, path = heapq.heappop(priority_queue)

        print(f"Current State: {current_state}, Cost: {cost}, Path: {path}")

        state_tuple = tuple(tuple(tube) for tube in current_state)
        if state_tuple in visited_states:
            print("State already visited, skipping.")
            continue
        visited_states.add(state_tuple)

        puzzle.tubes = copy.deepcopy(current_state)
        if puzzle.is_solved():
            print("Solution found!")
            return path

        valid_moves = puzzle.get_valid_moves()
        print(f"Valid Moves: {valid_moves}")
        for move in valid_moves:
            puzzle.tubes = copy.deepcopy(current_state)
            puzzle.apply_move(move)
            new_state = copy.deepcopy(puzzle.tubes)

            print(f"Applying Move: {move}")
            print(f"Resulting State: {new_state}")

            move_cost = 1
            heuristic_cost = puzzle.heuristic()
            total_cost = cost + move_cost + heuristic_cost
            new_path = path + [move]

            print(f"Move Cost: {move_cost}, Heuristic Cost: {heuristic_cost}, Total Cost: {total_cost}")

            heapq.heappush(priority_queue, (total_cost, cost + move_cost, new_state, new_path))

    print("No solution found.")
    return None


if __name__ == "__main__":
    initial_tubes = [
        ['B', 'F', 'D', 'B'],
        ['D', 'H', 'D', 'E'],
        ['A', 'H', 'C', 'D'],
        ['', '', '', ''],
        ['G', 'C', 'G', 'A'],
        ['A', 'B', 'G', 'E'],
        ['', '', '', ''],
        ['C', 'G', 'H', 'C'],
        ['F', 'F', 'B', 'E'],
        ['A', 'E', 'F', 'H'],
    ]

    puzzle = WaterSortPuzzle(initial_tubes)
    solution = a_star_solver(puzzle)

    if solution:
        print("Solution found!")
        for step, move in enumerate(solution, start=1):
            print(f"Step {step}: Move from tube {move[0] + 1} to tube {move[1] + 1}")
    else:
        print("No solution exists.")