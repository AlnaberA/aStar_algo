class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.open_set = set()
        self.closed_set = set()
        self.came_from = {}
        self.g_score = {}
        self.f_score = {}

    # Heuristic function: Manhattan distance for grid-based pathfinding
    def heuristic(self, node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def find_path(self, start, goal):
        self.open_set.add(start)
        self.g_score[start] = 0
        self.f_score[start] = self.heuristic(start, goal)

        while self.open_set:
            current = min(self.open_set, key=lambda x: self.f_score.get(x, float('inf')))
            if current == goal:
                return self.reconstruct_path(current)

            self.open_set.remove(current)
            self.closed_set.add(current)

            for neighbor in self.grid.get_neighbors(current):
                if neighbor in self.closed_set:
                    continue

                tentative_g_score = self.g_score.get(current, float('inf')) + 1

                if neighbor not in self.open_set:
                    self.open_set.add(neighbor)
                elif tentative_g_score >= self.g_score.get(neighbor, float('inf')):
                    continue

                self.came_from[neighbor] = current
                self.g_score[neighbor] = tentative_g_score
                self.f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)

        return []

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]