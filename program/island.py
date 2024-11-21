from tree import FIFOQueue, Problem

# Вам дана бинарная матрица, где 0 представляет воду, а 1 представляет землю.
# Связанные единицы формируют остров. Необходимо подсчитать общее
# количество островов в данной матрице. Острова могут соединяться как
# по вертикали и горизонтали, так и по диагонали.


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


def bfs_islands(problem, start, visited, new_grid, island_count):
    """Запускает поиск в ширину для поиска всех клеток одного острова."""
    if problem.is_land(start):
        new_grid[start[0]][start[1]] = island_count + 1
    frontier = FIFOQueue([start])
    visited.add(start)

    while frontier:
        node = frontier.pop()
        for action in problem.actions(node):
            if action not in visited and problem.is_land(action):
                visited.add(action)
                new_grid[action[0]][action[1]] = island_count + 1
                frontier.appendleft(action)
    return new_grid


def count_islands(grid):
    problem = IslandProblem(grid)
    visited = set()
    island_count = 0
    new_grid = grid.copy()

    for r in range(problem.rows):
        for c in range(problem.cols):
            state = (r, c)
            if state not in visited and problem.is_land(state):
                new_grid = bfs_islands(
                    problem, state, visited, new_grid, island_count
                )
                island_count += 1

    return island_count, new_grid


if __name__ == "__main__":
    # Пример использования
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1],
    ]

    island_count, new_grid = count_islands(grid)
    print("Количество островов:", island_count)
    for row in new_grid:
        print(row)

    # еще одна матрица 5 на 7
    grid2 = [
        [1, 1, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1],
    ]

    island_count, new_grid = count_islands(grid2)
    print("Количество островов:", island_count)
    for row in new_grid:
        print(row)
