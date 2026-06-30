import sympy as sp


def solve_dirrevative(derivative, order=1):

    x = sp.symbols("x")

    deri = sp.sympify(derivative)
    order = int(order) if str(order).isdigit() else 1
    return sp.diff(deri, x, order)
