import sympy as sp


def solve_equation(equation):
    x = sp.symbols("x")

    if "=" in equation:
        left_side, right_side = equation.split("=", 1)
        equation = sp.Eq(sp.sympify(left_side.strip()), sp.sympify(right_side.strip()))
    else:
        equation = sp.Eq(sp.sympify(equation.strip()), 0)

    return equation, x
