[README.md](https://github.com/user-attachments/files/29694823/README.md)
# Advanced Math Solver

### This project is an advanced math solver that can handle a variety of mathematical problems, it includes Equation solving, Differentiation, Integration, the solver is built using Python and leverages libraries such as Sympy and other mathematical libraries to provide accurate and efficient solutions, and visualization capabilities.

#### The engine is relies on three major pillars:

1. **SymPy:** is a Python library handles the "Thinking" and exact calculas/algebra manipulations.
2. **Numpy:** is a Pytohn library that handles the "Number Crunching" and numerical calculations.
3. **Matplotlib:** is a Python library that handles the "Visualization" and plotting of mathmetical functions and results.
4. **Streamlit:** is a Python library that handles the "User Interface" and provides an inteactive web application for users to input their mathematical problems and view the results.

## The Engine: How it works behind the scene

To understand why the app behaves the way it does, it helps to undestand one core function used throught the codebase: **'sp.lambdify'**

**The problem:** Sympy is designed for abstract math (like looking at $x^2$ as a symbol), but it's too slow to calculate thousands of individual coordinate points for a graph.
**The soultion:** We used 'lambdify' to translate Sympy's symbolic formals into lightining fast Python functions instantly.and Numpy can then pass thousands of numbers through this functions simultaneously,that allowing matplotlib to plot the results in a fraction of a second.

## Curcial points the user must know:

- **Exponents:** use '**' instead if '^'. (e.g., 'x**2' for '$x^2$', not 'x^2').
- **Multiplcation:** Always use ' * ' sign. (e.g., type '2*x', 'x\*sp.sin(x)', not '2x' or 'xsin(x)')

## The 2D Graph Limit (Real vs. Complex Numbers)

- The graphing canvas is a standard 2D Cartesian plane ($X$ and $Y$). It can only display **real numbers**.
- **Equations:** If you solve an equation like $x^2 + 4 = 0$, the algebraic output will correctly show complex roots ($[-2i, 2i]$). However, because these roots contain imaginary components, **they will not drop a visible marker on the graph's horizontal axis**, because the curve never physically crosses $y = 0$.
- **Calculus:** Functions that result in complex outputs over the plotted range cannot be drawn and will display a safe warning box rather than crashing the application.

## Understanding the Calculus Visuals

Each math module translates calculus concepts into visual geometry:

- **Derivatives:** The app plots the original function as a solid line and the derivative as a dashed line. This allows you to visually verify that wherever the original curve peaks or bottoms out, the derivative line crosses exactly through zero (signifying a slope of zero).
- **Definite Integration:** The app dynamically highlights the boundaries you input and fills the trapped space with a transparent color.
