def is_variable(term):
    return isinstance(term, str) and len(term) == 1 and term.islower()


def unify(x, y, subs):
    if x == y:
        return subs

    if is_variable(x):
        return unify_var(x, y, subs)

    if is_variable(y):
        return unify_var(y, x, subs)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x[1]) != len(y[1]):
            return None

        for a, b in zip(x[1], y[1]):
            subs = unify(a, b, subs)
            if subs is None:
                return None

        return subs

    return None


def unify_var(var, term, subs):
    if var in subs:
        return unify(subs[var], term, subs)

    if is_variable(term) and term in subs:
        return unify(var, subs[term], subs)

    if occurs(var, term, subs):
        return None

    subs[var] = term
    return subs


def occurs(var, term, subs):
    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, arg, subs) for arg in term[1])

    if is_variable(term) and term in subs:
        return occurs(var, subs[term], subs)

    return False


def parse(expr):
    name, rest = expr.replace(" ", "").split("(", 1)
    args = rest[:-1].split(",")

    return (name, tuple(
        parse(arg) if "(" in arg else arg
        for arg in args
    ))


def substitute(term, subs):
    if is_variable(term) and term in subs:
        return substitute(subs[term], subs)

    if isinstance(term, tuple):
        return (term[0], tuple(
            substitute(arg, subs) for arg in term[1]
        ))

    return term


def display(term):
    if isinstance(term, tuple):
        return term[0] + "(" + ", ".join(
            display(arg) for arg in term[1]
        ) + ")"
    return term


def main():
    cases = [
        ("Eats(x, Apple)", "Eats(Riya, y)"),
        ("Knows(John, x)", "Knows(x, Elizabeth)")
    ]

    for i, (e1, e2) in enumerate(cases, 1):
        print("\nCase", i)
        print("Expression 1:", e1)
        print("Expression 2:", e2)

        result = unify(parse(e1), parse(e2), {})

        if result is None:
            print("Unification failed.")
        else:
            print("Substitutions:")
            for var, value in result.items():
                print(var, "=", display(value))

            print("Unified Expression:",
                  display(substitute(parse(e1), result)))
            print("Unification successful.")


if __name__ == "__main__":
    main()
