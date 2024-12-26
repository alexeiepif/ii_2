#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any, Generator

from tree import Problem, breadth_first_search, path_actions, path_states

# Реализуйте алгоритм поиска в ширину (BFS) для решения задачи о льющихся
# кувшинах, где цель состоит в том, чтобы получить заданный объем воды
# в одном из кувшинов.


class PourProblem(Problem):
    def __init__(
        self, initial: tuple[int, int, int], goal: int, sizes: tuple[int, int, int]
    ) -> None:
        super().__init__(initial, goal)  # type: ignore
        self.sizes = sizes

    def actions(
        self, _: tuple[int, int, int]
    ) -> Generator[tuple[str, int] | tuple[str, int, int], None, None]:
        pour = (0, 1, 2)
        for i in pour:
            yield ("Fill", i)
            yield ("Dump", i)
            for j in pour:
                if i != j:
                    yield ("Pour", i, j)

    def result(
        self, state: tuple[int, int, int], action: tuple[Any]
    ) -> tuple[int, ...]:
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

    def is_goal(self, state: tuple[int, int, int]) -> bool:
        return self.goal in state  # type: ignore

    def action_cost(
        self,
        s: tuple[int, int, int],
        a: tuple[str, int] | tuple[str, int, int],
        s1: tuple[int, int, int],
    ) -> int:
        return 1


def solve(
    init: tuple[int, int, int], goal: int, sizes: tuple[int, int, int]
) -> tuple[int, list[tuple[int, int, int]], list[tuple[str, int]]]:
    problem = PourProblem(init, goal, sizes)
    b = breadth_first_search(problem)
    length = b.path_cost
    path = path_states(b)  # type: ignore
    actions = path_actions(b)  # type: ignore
    return length, path, actions


if __name__ == "__main__":
    initial = (1, 1, 1)
    goal = 13
    sizes = (2, 16, 32)
    length, path, actions = solve(initial, goal, sizes)
    print("Длина наименьшего решения:", length)
    print("Кратчайшее решение:", path)
    print("Действия:", actions)
