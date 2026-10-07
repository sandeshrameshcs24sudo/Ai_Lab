import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Heuristic: Manhattan Distance
def h(state):
    distance = 0

    for i in range(9):

        tile = state[i]

        if tile != 0:

            # Current position
            current_row = i // 3
            current_col = i % 3

            # Goal position
            goal_index = tile - 1
            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Generate neighboring states
def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_blank = r * 3 + c

            new_state = list(state)
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search
def a_star(start):
    pq = []

    # (f, g, state, path)
    heapq.heappush(pq, (h(start), 0, start, [start]))

    visited = {start: 0}

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        for next_state in get_neighbors(state):

            new_g = g + 1

            if next_state not in visited or new_g < visited[next_state]:

                visited[next_state] = new_g

                # f(n) = g(n) + h(n)
                new_f = new_g + h(next_state)

                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state, path + [next_state])
                )

    return None


def print_state(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()


# Input
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

path = a_star(start)

print("A* - Manhattan Distance")
print("Number of moves:", len(path) - 1)
print()

for state in path:
    print_state(state)
