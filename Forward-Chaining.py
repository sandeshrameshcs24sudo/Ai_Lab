def is_variable(term):
    return isinstance(term, str) and len(term) == 1 and term.islower()


def match(pattern, fact, theta):
    if len(pattern) != len(fact) or pattern[0] != fact[0]:
        return None

    theta = theta.copy()

    for p, f in zip(pattern[1:], fact[1:]):
        if is_variable(p):
            if p in theta and theta[p] != f:
                return None
            theta[p] = f
        elif p != f:
            return None

    return theta


def find_substitutions(conditions, facts, theta=None):
    if theta is None:
        theta = {}

    if not conditions:
        return [theta]

    results = []

    for fact in facts:
        new_theta = match(conditions[0], fact, theta)

        if new_theta is not None:
            results.extend(
                find_substitutions(
                    conditions[1:], facts, new_theta
                )
            )

    return results


def forward_chaining(facts, rules, query):
    facts = list(facts)

    changed = True
    while changed:
        changed = False

        for conditions, conclusion in rules:
            substitutions = find_substitutions(
                conditions, facts
            )

            for theta in substitutions:
                new_fact = tuple(
                    theta.get(term, term)
                    if is_variable(term) else term
                    for term in conclusion
                )

                if new_fact not in facts:
                    facts.append(new_fact)
                    changed = True
                    print("Inferred:", new_fact)

                if new_fact == query:
                    return True

        if query in facts:
            return True

    return query in facts


def main():
    rules = [
        ([("Missile", "x")],
         ("Weapon", "x")),

        ([("Enemy", "x", "America")],
         ("Hostile", "x")),

        ([("Missile", "x"), ("Owns", "A", "x")],
         ("Sells", "Robert", "x", "A")),

        ([("American", "p"), ("Weapon", "q"),
          ("Sells", "p", "q", "r"), ("Hostile", "r")],
         ("Criminal", "p"))
    ]

    query = ("Criminal", "Robert")

    # Case 1: All required facts are available
    facts1 = [
        ("American", "Robert"),
        ("Owns", "A", "T1"),
        ("Missile", "T1"),
        ("Enemy", "A", "America")
    ]

    # Case 2: Enemy fact is missing
    facts2 = [
        ("American", "Robert"),
        ("Owns", "A", "T1"),
        ("Missile", "T1")
    ]

    for i, facts in enumerate([facts1, facts2], 1):
        print("\nCASE", i)
        print("Query: Criminal(Robert)")

        if forward_chaining(facts, rules, query):
            print("Result: Query proved.")
        else:
            print("Result: Query cannot be proved.")


if __name__ == "__main__":
    main()
                 