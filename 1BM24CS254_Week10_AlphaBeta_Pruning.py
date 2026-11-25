from math import inf

tree = [
    [[10, 9], [14, 18]],
    [[5, 4], [50, 3]]
]

visited = []
pruned = []

def alpha_beta(node, alpha, beta, maximizing, path="Root[MAX]"):
    if isinstance(node, int):
        visited.append(node)
        print("Visited leaf:", node)
        return node

    value = -inf if maximizing else inf

    for i, child in enumerate(node):
        side = "Left" if i == 0 else "Right"

        if isinstance(child, list):
            role = "MIN" if maximizing else "MAX"
            child_path = f"{path} -> {side}[{role}]"
        else:
            child_path = f"{path} -> {side}[leaf={child}]"

        result = alpha_beta(
            child, alpha, beta, not maximizing, child_path
        )

        if maximizing:
            value = max(value, result)
            alpha = max(alpha, value)
        else:
            value = min(value, result)
            beta = min(beta, value)

        if alpha >= beta:
            for j in range(i + 1, len(node)):
                remaining = node[j]
                side2 = "Left" if j == 0 else "Right"

                if isinstance(remaining, list):
                    role2 = "MIN" if maximizing else "MAX"
                    desc = (
                        f"{path} -> {side2}[{role2}] "
                        f"subtree {remaining}"
                    )
                else:
                    desc = (
                        f"{path} -> {side2}[leaf={remaining}]"
                    )

                pruned.append(desc)
                print("Pruned:", desc)

            break

    return value


result = alpha_beta(tree, -inf, inf, True)

print("\nRoot value:", result)
print("Visited leaves:", visited)
print("Optimal path: Root -> Left MIN -> Left MAX -> leaf 10")