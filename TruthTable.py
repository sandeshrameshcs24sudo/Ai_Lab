from itertools import product

# Implication: A -> B
def implies(a, b):
    return (not a) or b


# Knowledge Base: (Q -> P) AND (P -> NOT Q) AND (Q OR R)
def KB(P, Q, R):
    return (
        implies(Q, P)
        and implies(P, not Q)
        and (Q or R)
    )


# Truth-table enumeration algorithm
def entails(query):
    for P, Q, R in product([True, False], repeat=3):

        # Check only models where KB is true
        if KB(P, Q, R):
            if not query(P, Q, R):
                return False

    return True


# Display truth table
print("P Q R | Q->P P->~Q Q|R | KB")
print("--------------------------------")

for P, Q, R in product([True, False], repeat=3):
    a = implies(Q, P)
    b = implies(P, not Q)
    c = Q or R
    kb_value = KB(P, Q, R)

    def tf(value):
        return "T" if value else "F"

    print(
        tf(P), tf(Q), tf(R), "|",
        tf(a), "   ", tf(b), " ", tf(c), "|",
        tf(kb_value)
    )


# Test the three queries
print("\nQuery 1: KB entails R:",
      entails(lambda P, Q, R: R))

print("Query 2: KB entails (R -> P):",
      entails(lambda P, Q, R: implies(R, P)))

print("Query 3: KB entails (Q -> R):",
      entails(lambda P, Q, R: implies(Q, R)))