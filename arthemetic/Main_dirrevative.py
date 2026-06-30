import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from dirrevative import solve_dirrevative

x = sp.symbols("x")


def direvative():
    st.header("Solve Derivative")
    st.info(
        "structure: `x**2` or `e**x` (If you want to specify the order, use the format: `function, order`)"
    )
    dinp = st.text_input("Enter your function:").lower().strip()
    order = st.number_input(
        "Enter the order of the derivative (default is 1):",
        min_value=1,
        max_value=10,
        step=1,
    )
    if st.button("Solve Derivative"):
        try:
            derrs = sp.sympify(dinp)
            res = solve_dirrevative(derrs, order)
            st.latex(f"{sp.latex(derrs)}")
            st.latex(f"Order = {order}")
            st.latex(f"Derivative = {sp.latex(res)}")
            # Visualization

            f_fun = sp.lambdify(x, derrs, modules=["numpy", "math"])
            df_fun = sp.lambdify(x, res, modules=["numpy", "math"])

            x_vals = np.linspace(-5, 5, 400)

            try:
                y_f = f_fun(x_vals)
                y_df = df_fun(x_vals)

                if np.isscalar(y_f):
                    y_f = np.full_like(x_vals, y_f)
                if np.isscalar(y_df):
                    y_df = np.full_like(x_vals, y_df)

                fig, ax = plt.subplots()

                ax.plot(
                    x_vals,
                    y_f,
                    label=f"Original f(x) = {sp.latex(derrs)}",
                    color="blue",
                    linewidth=2,
                )

                ax.plot(
                    x_vals,
                    y_df,
                    label=f"Derivative f^({order})(x) = {sp.latex(res)}",
                    color="red",
                    linestyle="--",
                    linewidth=2,
                )

                ax.axhline(0, color="black", linewidth=0.8)
                ax.axvline(0, color="black", linewidth=0.8)
                ax.grid(True, linestyle=":", alpha=0.6)
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.set_title(f"Function and its Derivative (Order {order})")
                ax.legend()

                st.pyplot(fig)

            except Exception as plot_err:
                st.warning(
                    f"Could not generate a visual plot for this function over the standard range: {plot_err}"
                )

        except ValueError:
            st.error("Invalid input. Please enter a valid function.")
