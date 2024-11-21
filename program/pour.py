from tree import Problem, breadth_first_search, path_actions, path_states

# Реализуйте алгоритм поиска в ширину (BFS) для решения задачи о льющихся
# кувшинах, где цель состоит в том, чтобы получить заданный объем воды
# в одном из кувшинов.


class PourProblem(Problem):
    def __init__(self, initial: tuple, goal: int, sizes: tuple):
        super().__init__(initial, goal)
        self.sizes = sizes

    def actions(self, _):
        pour = (0, 1, 2)
        for i in pour:
            yield ("Fill", i)
            yield ("Dump", i)
            for j in pour:
                if i != j:
                    yield ("Pour", i, j)

    def result(self, state: tuple, action: tuple):
        list_state = list(state)
        match action:
            case ("Fill", i):
                list_state[i] = self.sizes[i]
            case ("Dump", i):
                list_state[i] = 0
            case ("Pour", i, j):
                diff = list_state[i] - (self.sizes[j] - list_state[j])
                if diff > 0:
                    list_state[i] = diff
                    list_state[j] = self.sizes[j]
                else:
                    list_state[j] += list_state[i]
                    list_state[i] = 0
        return tuple(list_state)

    def is_goal(self, state: tuple):
        return self.goal in state

    def action_cost(self, *_):
        return 1


def search(problem: Problem):
    b = breadth_first_search(problem)
    length = b.path_cost
    path = path_states(b)
    actions = path_actions(b)
    return length, path, actions


def solve(init: tuple, goal: int, sizes: tuple):
    problem = PourProblem(init, goal, sizes)
    return search(problem)


if __name__ == "__main__":
    initial = (1, 1, 1)
    goal = 13
    sizes = (2, 16, 32)
    length, path, actions = solve(initial, goal, sizes)
    print("Длина наименьшего решения:", length)
    print("Кратчайшее решение:", path)
    print("Действия:", actions)
