import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import sympy as sp
from integration import solve_integration

x = sp.symbols("x")


def solve_integrate():
    st.header("Solve Integration")
    st.info(
        "structure: `x**2` or `e**x` (If you want to specify the limits, use the format: `function, lower_limit, upper_limit`)"
    )
    iiinput = st.text_input("Enter your function:").lower().strip()
    integration_type = st.selectbox(
        "Select the type of integration:", ["Indefinite", "Definite"]
    )
    if integration_type == "Indefinite":
        if st.button("Solve Integration"):
            try:
                spmy = sp.sympify(iiinput)
                res = solve_integration(iiinput, integration_type="indefinite")
                st.latex(f"{sp.latex(spmy)} = {sp.latex(res)} + C")
                # Visualization
                f_fun = sp.lambdify(x, spmy, modules=["numpy", "math"])
                F_fun = sp.lambdify(x, res, modules=["numpy", "math"])
                x_vals = np.linspace(-5, 5, 400)
                try:
                    y_f = f_fun(x_vals)
                    y_F = F_fun(x_vals)

                    if np.isscalar(y_f):
                        y_f = np.full_like(x_vals, y_f)

                    if np.isscalar(y_F):
                        y_F = np.full_like(x_vals, y_F)

                    fig, ax = plt.subplots()
                    ax.plot(
                        x_vals,
                        y_f,
                        label=f"f(x) = {sp.latex(spmy)}",
                        color="blue",
                        linewidth=2,
                    )

                    ax.plot(
                        x_vals,
                        y_F,
                        label=f"anti-derivative F(x) = {sp.latex(res)}",
                        color="orange",
                        linestyle="-.",
                        linewidth=2,
                    )

                    ax.axhline(0, color="black", linewidth=0.8)
                    ax.axvline(0, color="black", linewidth=0.8)
                    ax.grid(True, linestyle=":", alpha=0.6)
                    ax.set_title(
                        "Function and its Indefinite Integral (Antiderivative)"
                    )
                    ax.legend()
                    st.pyplot(fig)

                except Exception:
                    st.warning("Could not generate graph over the default range.")

            except ValueError:
                st.error("Invalid input. Please enter a valid function.")
    elif integration_type == "Definite":
        col1, col2 = st.columns(2)
        with col1:
            lower_limit = st.text_input("Enter the lower limit:")
        with col2:
            upper_limit = st.text_input("Enter the upper limit:")

        if st.button("Solve Integration"):
            try:
                res = solve_integration(
                    iiinput,
                    integration_type="definite",
                    lower_limit=lower_limit,
                    upper_limit=upper_limit,
                )
                spmy = sp.sympify(iiinput)

                st.latex(f"{sp.latex(spmy)} = {sp.latex(res)} + C")

                # Visualization
                f_fun = np.lambdify(x, spmy, modules=["math", "numpy"])

                try:
                    a = float(sp.N(sp.sympify(lower_limit)))
                    b = float(sp.N(sp.sympify(upper_limit)))

                    margin = max(1.0, abs(b - a) * 0.25)
                    x_vals = np.linspace(a - margin, b + margin, 400)
                    x_shade = np.linspace(a, b, 200)

                    y_vals = f_fun(x_vals)
                    y_shade = f_fun(x_shade)

                    if np.isscalar(y_vals):
                        y_vals = np.full_like(x_vals, y_vals)
                    if np.isscalar(y_shade):
                        y_shade = np.full_like(x_shade, y_shade)

                    fig, ax = plt.subplots()
                    ax.plot(
                        x_vals,
                        y_vals,
                        label=f"f(x) = {sp.latex(spmy)}",
                        color="blue",
                        linewidth=2,
                    )
                    area_label = (
                        f"Area ≈ {float(sp.N(res)):.4f}"
                        if res.is_Number
                        else "Area under curve"
                    )
                    ax.fill_between(
                        x_shade,
                        y_shade,
                        color="green",
                        alpha=0.3,
                        label=area_label,
                    )
                    ax.axvline(
                        a,
                        color="darkgreen",
                        linestyle=":",
                        label=f"Start (x={lower_limit})",
                    )
                    ax.axvline(
                        b,
                        color="darkred",
                        linestyle=":",
                        label=f"End (x={upper_limit})",
                    )

                    ax.axhline(0, color="black", linewidth=0.8)
                    ax.grid(True, linestyle=":", alpha=0.6)
                    ax.set_title(
                        f"Definite Integral Bounded Area from {lower_limit} to {upper_limit}"
                    )
                    ax.set_xlabel("x")
                    ax.set_ylabel("y")
                    ax.legend()

                    st.pyplot(fig)
                except Exception:
                    st.warning(
                        "Could not generate a bounded plot (ensure limits are real numbers)."
                    )

            except ValueError:
                st.error("Invalid input. Please enter a valid function and limits.")
