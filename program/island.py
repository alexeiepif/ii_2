from tree import FIFOQueue, Problem


class IslandProblem(Problem):
    def __init__(self, grid):
        super().__init__(initial=None)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def actions(self, state):
        r, c = state
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),  # Вверх, вниз, влево, вправо
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]  # Диагонали
        return [
            (r + dr, c + dc)
            for dr, dc in directions
            if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols
        ]

    def is_land(self, state):

        r, c = state
        return self.grid[r][c] == 1


def bfs_islands(problem, start, visited):
    """Запускает поиск в ширину для поиска всех клеток одного острова."""
    frontier = FIFOQueue([start])
    visited.add(start)

    while frontier:
        node = frontier.pop()
        for action in problem.actions(node):
            if action not in visited and problem.is_land(action):
                visited.add(action)
                frontier.appendleft(action)
    return visited


def count_islands(grid):
    problem = IslandProblem(grid)
    visited = set()
    island_count = 0

    for r in range(problem.rows):
        for c in range(problem.cols):
            state = (r, c)
            if state not in visited and problem.is_land(state):
                bfs_islands(problem, state, visited)
                island_count += 1

    return island_count


if __name__ == "__main__":
    # Пример использования
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1],
    ]

print("Количество островов:", count_islands(grid))
