# filepath: /a_star_visualizer/a_star_visualizer/src/main.py

import pygame
from algorithms.a_star import AStar
from utils.grid import Grid
from visualization.visualizer import Visualizer

def main():
    pygame.init()
    
    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("A* Algorithm Visualizer")
    
    # Initialize grid and visualizer
    grid = Grid()
    grid.create_grid(20, 15)  # Example grid size
    visualizer = Visualizer(screen, grid)
    
    # Initialize A* algorithm
    a_star = AStar(grid)

    # Main loop
    running = True
    start_set, goal_set = False, False
    path_found = False
    path = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x // visualizer.cell_width, y // visualizer.cell_height

                if not start_set:
                    grid.set_cell(grid_x, grid_y, Grid.START)
                    start = (grid_x, grid_y)
                    start_set = True
                elif not goal_set:
                    grid.set_cell(grid_x, grid_y, Grid.GOAL)
                    goal = (grid_x, grid_y)
                    goal_set = True
                else:
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

        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()