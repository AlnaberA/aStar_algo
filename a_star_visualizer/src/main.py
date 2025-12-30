import pygame
from algorithms.a_star import AStar
from utils.grid import Grid
from visualization.visualizer import Visualizer

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.is_active = False

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def main():
    pygame.init()
    
    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("A* Algorithm Visualizer")
    font = pygame.font.Font(None, 24)
    
    # Initialize grid and visualizer
    grid = Grid()
    grid.create_grid(20, 13)  # Adjusted grid size to accommodate buttons
    visualizer = Visualizer(screen, grid)
    
    # Initialize A* algorithm
    a_star = AStar(grid)

    # Create buttons
    start_button = Button(50, 530, 100, 40, "Set Start", (100, 200, 100), (255, 255, 255))
    end_button = Button(200, 530, 100, 40, "Set End", (200, 100, 100), (255, 255, 255))

    # Main loop
    running = True
    start_set, goal_set = False, False
    path_found = False
    path = []
    start = None
    goal = None
    mode = None  # 'start', 'end'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                # Check button clicks
                if start_button.is_clicked((x, y)):
                    mode = 'start'
                    start_button.is_active = True
                    end_button.is_active = False
                elif end_button.is_clicked((x, y)):
                    mode = 'end'
                    end_button.is_active = True
                    start_button.is_active = False
                else:
                    # Click on grid
                    grid_x, grid_y = x // visualizer.cell_width, y // visualizer.cell_height
                    
                    # Check bounds
                    if 0 <= grid_x < 20 and 0 <= grid_y < 13:
                        if mode == 'start' and grid.get_cell(grid_x, grid_y) == Grid.EMPTY:
                            grid.set_cell(grid_x, grid_y, Grid.START)
                            start = (grid_x, grid_y)
                            start_set = True
                            mode = None
                            start_button.is_active = False
                        elif mode == 'end' and grid.get_cell(grid_x, grid_y) == Grid.EMPTY:
                            grid.set_cell(grid_x, grid_y, Grid.GOAL)
                            goal = (grid_x, grid_y)
                            goal_set = True
                            mode = None
                            end_button.is_active = False
                        elif mode is None and grid.get_cell(grid_x, grid_y) == Grid.EMPTY:
                            grid.set_cell(grid_x, grid_y, Grid.OBSTACLE)

        # If both start and goal are set, execute A* algorithm
        if start_set and goal_set and not path_found:
            path = a_star.find_path(start, goal)
            path_found = True

        # Draw the grid
        visualizer.draw_grid()

        # Highlight the path if found
        if path_found:
            visualizer.update_visualization(path)

        # Draw buttons
        start_button.draw(screen, font)
        end_button.draw(screen, font)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()