import random
import math

N = 8

def conflicts(board):
    count = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (board[i] == board[j] or
                abs(board[i] - board[j]) == abs(i - j)):
                count += 1

    return count


def neighbor(board):
    next_board = board.copy()
    col = random.randrange(N)
    row = random.randrange(N - 1)

    if row >= next_board[col]:
        row += 1

    next_board[col] = row
    return next_board


def simulated_annealing():
    for restart in range(100):
        current = [random.randrange(N) for _ in range(N)]
        cost = conflicts(current)
        temperature = 5.0

        while temperature > 0.001:
            if cost == 0:
                return current

            next_state = neighbor(current)
            next_cost = conflicts(next_state)

            delta_e = cost - next_cost

            if (delta_e > 0 or
                random.random() < math.exp(delta_e / temperature)):
                current = next_state
                cost = next_cost

            temperature *= 0.999

        if cost == 0:
            return current

    return None


random.seed(42)
solution = simulated_annealing()

if solution is not None:
    print("Solution:", solution)
    print("Number of conflicts:", conflicts(solution))
    print("Board:")

    for row in range(N):
        print(" ".join(
            "Q" if solution[col] == row else "."
            for col in range(N)
        ))
else:
    print("Solution not found.")