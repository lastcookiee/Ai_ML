import heapq

# Manhattan distance heuristic
def manhattan(puzzle, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0:
                x, y = divmod(goal.index(puzzle[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# A* Search
def a_star_search(start, goal):
    start_tuple = tuple(tuple(row) for row in start)
    goal_tuple = tuple(goal)
    pq = [(manhattan(start, goal_tuple), 0, start_tuple, [])]
    visited = set()
    
    while pq:
        _, g, current, path = heapq.heappop(pq)
        visited.add(current)
        
        if current == goal_tuple:
            return path + [current]
        
        for neighbor, move in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(pq, (g + 1 + manhattan(neighbor, goal_tuple), g + 1, neighbor, path + [current]))
    
    return None

# Get possible moves
def get_neighbors(puzzle):
    neighbors = []
    x, y = [(i, j) for i in range(3) for j in range(3) if puzzle[i][j] == 0][0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_puzzle = [list(row) for row in puzzle]
            new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
            neighbors.append((tuple(tuple(row) for row in new_puzzle), f"Move {puzzle[nx][ny]} to ({x}, {y})"))
    
    return neighbors

# Display the puzzle
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

# Check if the puzzle is solvable
def is_solvable(puzzle):
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

# Initial state
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Goal state
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Check if the puzzle is solvable
if is_solvable(start):
    # Run A* Search
    solution = a_star_search(start, goal)

    # Print the solution
    if solution:
        print("Solution found!")
        for step in solution:
            print_puzzle(step)
    else:
        print("No solution exists.")
else:
    print("The puzzle is not solvable.")
