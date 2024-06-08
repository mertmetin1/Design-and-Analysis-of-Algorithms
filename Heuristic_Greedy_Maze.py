class Maze:
    def __init__(self, grid, start, exit):
        self.grid = grid
        self.start = start
        self.exit = exit
        self.current_position = start
    
    def get_neighbors(self, position):
        neighbors = []
        x, y = position
        # Define possible moves: up, down, left, right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if self.is_valid_position((new_x, new_y)):
                neighbors.append((new_x, new_y))
        return neighbors
    
    def is_valid_position(self, position):
        x, y = position
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return self.grid[x][y] != '#'
        return False
    
    def euclidean_distance(self, position1, position2):
        return ((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2) ** 0.5
    
    def move(self):
        neighbors = self.get_neighbors(self.current_position)
        if not neighbors:
            return False
        # Select the neighbor with the minimum distance to the exit
        next_position = min(neighbors, key=lambda pos: self.euclidean_distance(pos, self.exit))
        self.current_position = next_position
        return True
    
    def solve(self):
        while self.current_position != self.exit:
            if not self.move():
                return False
        return True

# Example usage
maze_grid = [
    ['C', ' ', ' ', ' '],
    ['#', '#', ' ', '#'],
    [' ', ' ', ' ', 'E']
]
start = (0, 0)
exit = (2, 3)

maze = Maze(maze_grid, start, exit)
if maze.solve():
    print("Exit found!")
else:
    print("No path to exit.")
