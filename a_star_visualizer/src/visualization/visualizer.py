import pygame
from utils.grid import Grid

class Visualizer:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.cell_width = screen.get_width() // len(grid.grid[0])
        self.cell_height = screen.get_height() // len(grid.grid)

    COLORS = {
        Grid.EMPTY: (255, 255, 255),  # White
        Grid.START: (0, 0, 255),      # Blue
        Grid.GOAL: (255, 0, 0),       # Red
        Grid.OBSTACLE: (0, 0, 0),     # Black
    }

    def draw_grid(self):
        for y, row in enumerate(self.grid.grid):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                color = self.COLORS[cell]
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)  # Grid lines

    def update_visualization(self, path):
        """Updates the visualization by highlighting the path."""
        for node in path:
            x, y = node
            # Skip coloring the goal node to keep it red
            if self.grid.get_cell(x, y) == Grid.GOAL:
                continue
            # Skip coloring the start node to keep it blue
            if self.grid.get_cell(x, y) == Grid.START:
                continue
            rect = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
            pygame.draw.rect(self.screen, (0, 255, 0), rect)  # Green for the path

    def run(self):
        """Main loop for running the visualizer."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_grid()
            pygame.display.flip()

        pygame.quit()