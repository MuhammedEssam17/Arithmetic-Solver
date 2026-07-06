import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from Equation import solve_equation


def solve_equation_s():
    st.header("Solve Equation")
    st.info(
        "structure: `x**2 - 4*x + 4 = 0` or `2*x + 3 = x - 5` (If there is no '=', it will be '= 0' as default)"
    )
    # Input for the equation
    inpequ = st.text_input("Enter your equation:").lower().strip()
    if st.button("Solve Equation"):
        try:
            # Equation solving
            equation, x = solve_equation(inpequ)
            sol = sp.solve(equation, x)

            # Displaying the results in streamlit as latex format
            st.latex(f"{sp.latex(equation)} ")
            st.latex(f"X = {sp.latex(sol)} ")

            # Visualization
            # first define the function f(x) = lhs - rhs
            to_plot = equation.lhs - equation.rhs
            f_fun = sp.lambdify(x, to_plot, modules=["numpy", "math"])

            rel_solution = []
            has_complex = False
            for s in sol:
                if s.is_real:
                    rel_solution.append(float(sp.N(s)))
                else:
                    has_complex = True

            if rel_solution:
                xmin = min(rel_solution) - 3
                xmax = max(rel_solution) + 3
                if xmin == xmax:
                    xmin -= 2
                    xmax += 2
            else:
                xmin, xmax = -5, 5

            x_vals = np.linspace(xmin, xmax, 400)

            try:
                y_vals = f_fun(x_vals)
                # Handle scalar output for constant equations
                if np.isscalar(y_vals):
                    y_vals = np.full_like(x_vals, y_vals)

                fig, ax = plt.subplots()
                ax.plot(
                    x_vals,
                    y_vals,
                    label=f"f(x) = {sp.latex(to_plot)}",
                    color="red",
                    linewidth=2,
                )
                ax.axhline(0, color="black", linewidth=1.2)  # x axis
                ax.axvline(0, color="black", linewidth=0.5)  # y axis

                # Plotting the roots if they exist
                if rel_solution:
                    ax.scatter(
                        rel_solution,
                        [0] * len(rel_solution),
                        color="red",
                        s=50,
                        zorder=5,
                        label="Roots",
                    )
                    for r in rel_solution:
                        ax.annotate(
                            f"({r:.2f}, 0)",
                            (r, 0),
                            textcoords="offset points",
                            xytext=(0, 10),
                            ha="center",
                            color="blue",
                            weight="bold",
                        )
                # If the root is complex
                if has_complex and not rel_solution:
                    ax.set_title(
                        "Equation Graph (Complex and imaginary roots are not shown in plot)"
                    )
                else:
                    ax.set_title("Equation Graph")
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.set_xlabel("x")
                ax.set_ylabel("f(x)")
                ax.set_title("Equation Graph")
                ax.legend()
                st.pyplot(fig)
            except Exception:
                st.warning(
                    "Could not generate a plot for this complex or non-numeric equation range."
                )

        except ValueError:
            st.error("Invalid input. Please enter a valid equation.")
