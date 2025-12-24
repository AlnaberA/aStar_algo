class Grid:
    # Define constants for cell states
    EMPTY = 0
    START = 1
    GOAL = 2
    OBSTACLE = 3

    def __init__(self):
        self.grid = []

    def create_grid(self, width, height):
        """Creates a grid with the specified width and height."""
        self.grid = [[self.EMPTY for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, state):
        """Sets the state of a specific cell."""
        self.grid[y][x] = state

    def get_cell(self, x, y):
        """Gets the state of a specific cell."""
        return self.grid[y][x]

    def get_neighbors(self, node):
        """Returns a list of valid neighboring cells for the given node."""
        x, y = node
        neighbors = []

        # Define possible moves (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the neighbor is within bounds
            if 0 <= ny < len(self.grid) and 0 <= nx < len(self.grid[0]):
                # Check if the neighbor is not an obstacle
                if self.grid[ny][nx] != self.OBSTACLE:
                    neighbors.append((nx, ny))

        return neighbors