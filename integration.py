import sympy as sp


def solve_integration(
    integration, integration_type="indefinite", lower_limit=None, upper_limit=None
):

    x = sp.symbols("x")
    integ = sp.sympify(integration)

    if integration_type == "indefinite":
        return sp.integrate(integ, x)

    elif integration_type == "definite":

        lower_limit = sp.sympify(lower_limit)
        upper_limit = sp.sympify(upper_limit)
        return sp.integrate(integ, (x, lower_limit, upper_limit))
