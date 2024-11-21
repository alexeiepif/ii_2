from tree import Problem, breadth_first_search, path_states

# Вам предоставлен код для поиска кратчайшего пути через лабиринт,
# используя алгоритм поиска в ширину (BFS). Лабиринт представлен
# в виде бинарной матрицы, где 1 обозначает проход, а 0 — стену.
# Необходимо модифицировать и дополнить код, чтобы реализовать
# полный функционал поиска пути.


class MazeProblem(Problem):
    def __init__(self, maze, initial, goal):
        super().__init__(initial=initial, goal=goal)
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if self.rows > 0 else 0

    def actions(self, state):
        r, c = state
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            if (
                0 <= r + dr < self.rows
                and 0 <= c + dc < self.cols
                and self.maze[r + dr][c + dc] != 0
            ):
                yield (r + dr, c + dc)

    def is_goal(self, state):
        return state == self.goal

    def result(self, state, action):
        return action

    def action_cost(self, s, a, s1):
        return 1


def search(problem):
    b = breadth_first_search(problem)
    length = b.path_cost
    path = path_states(b)
    return length, path


def solve(maze, start, goal):
    problem = MazeProblem(maze, start, goal)
    return search(problem)


if __name__ == "__main__":
    maze = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    ]
    initial = (0, 0)
    goal = (7, 5)
    length, path = solve(maze, initial, goal)
    print("Длина кратчайшего пути:", length)
    print("Кратчайший путь:", path)

    # еще одна матрица 10 на 10
    print("Еще один лабиринт")
    maze2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    ]

    initial = (9, 9)
    goal = (0, 0)

    length, path = solve(maze2, initial, goal)
    print("Длина кратчайшего пути:", length)
    print("Кратчайший путь:", path)
