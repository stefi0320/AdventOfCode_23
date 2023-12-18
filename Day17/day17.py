from pathlib import Path
import time
import heapq
from typing import Self

class Node:
    def __init__(
        self,
        heat_lost: int,
        pos: tuple[int, int],
        steps: int,
        direction: str,
    ):
        self.heat_lost = heat_lost
        self.pos = pos
        self.steps = steps
        self.direction = direction
           

    def to_hashable(self) -> tuple[tuple[int, int], int, str]:
        return (self.pos, self.steps, self.direction)

    # For heapq
    def __lt__(self, other):
        return self.heat_lost < other.heat_lost

    # For visited
    def __hash__(self):
        return hash(self.to_hashable())

    def __eq__(self, other):
        return self.to_hashable() == other.to_hashable()

    def __repr__(self):
        return f"Node(heat_lost={self.heat_lost}, pos={self.pos}, steps={self.steps}, direction={self.direction})"
        
    def get_neighbours(self, m, n, min_step, max_step) -> list[Self]:
        neighbour_list = []
        invalid_steps = {'L': 'R', 'R': 'L', 'D': 'U', 'U': 'D'}
        for di, dj, d in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            if (d in invalid_steps[self.direction] or
                (d == self.direction and self.steps >= max_step) or 
                (d != self.direction and self.steps < min_step)):
                continue
            ni, nj = self.pos[0] + di, self.pos[1] + dj
            if 0 <= ni < m and 0 <= nj < n:
                if d == self.direction:
                    neighbour_list.append(Node(0, (ni, nj), self.steps + 1, d))
                else:
                    neighbour_list.append(Node(0, (ni, nj), 1, d))
        return neighbour_list


class Grid:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.queue = [
            Node(heat_lost=0, pos=(0, 0), steps=0, direction='R'),
            Node(heat_lost=0, pos=(0, 0), steps=0, direction='D'),
        ]
        
    def get_heat_lost(self, position: tuple[int, int]) -> int:
        x, y = position
        return self.grid[x][y]
    
    def shortes_path(self, min_step, max_step) -> int:       
        seen = set()
        while self.queue:
            current_node = heapq.heappop(self.queue)
            if current_node.pos == (self.height - 1, self.width- 1):
                if current_node.steps < min_step:
                    continue
                return current_node.heat_lost
            
            if current_node in seen:
                continue

            seen.add(current_node)

            for node in current_node.get_neighbours(self.height, self.width, min_step ,max_step):    
                new_heat_lost = current_node.heat_lost + self.get_heat_lost(node.pos)
                node.heat_lost = new_heat_lost
                heapq.heappush(self.queue, node)

        raise ValueError("No path found")

def open_file_safely(file_name):
    """ File open """
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r', encoding="utf-8") as file:
            content = [line.strip() for line in file]
        return content

    except FileNotFoundError:
        print(
            "The file '{file_name}' was not found in the same directory as the script.")
        return None

def day17():
    """Day 17 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day17.txt")
    
    tmp_grid = []
    for line in input_txt:
        tmp_grid.append([int(x) for x in line.strip()])
    lava_grid = Grid(tmp_grid)
    path_sum = lava_grid.shortes_path(0, 3)   
    print('Part 1: ', path_sum)
    lava_grid = Grid(tmp_grid)
    path_sum = lava_grid.shortes_path(4, 10)  
    print('Part 2: ', path_sum)
    
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day17()