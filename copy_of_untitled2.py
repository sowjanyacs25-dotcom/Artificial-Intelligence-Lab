

def dfs(start, goal, max_depth=9):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if len(path) - 1 >= max_depth:
            continue

        visited.add(state)

        zero = state.index(0)
        row, col = divmod(zero, 3)

        # Right, Down, Left, Up
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = list(state)
                new_zero = nr * 3 + nc

                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:
                    stack.append((new_state, path + [new_state]))

    return None


start = (2, 3, 0,
         1, 5, 6,
         4, 7, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = dfs(start, goal, 9)

if solution:
    print("DFS Solution")
    print("------------")

    for i, state in enumerate(solution):
        print("Step", i)
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()

output

Step 0
2 3 0
1 5 6
4 7 8

Step 1
2 0 3
1 5 6
4 7 8

Step 2
0 2 3
1 5 6
4 7 8

Step 3
1 2 3
0 5 6
4 7 8

Step 4
1 2 3
4 5 6
0 7 8

Step 5
1 2 3
4 5 6
7 0 8

Step 6
1 2 3
4 5 6
7 8 0

Total Steps: 7

print("\nSolution Path:", " -> ".join(path))
print("Steps:", len(path) - 1)
