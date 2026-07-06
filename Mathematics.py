import streamlit as st

from Main_Equation import solve_equation_s
from Main_dirrevative import direvative
from Main_integrate import solve_integrate

st.set_page_config(page_title="Math solver", page_icon="🌟", layout="centered")

section = st.sidebar.selectbox(
    "Select a section", ["Equation", "Derivative", "Integration"]
)

if section == "Equation":
    solve_equation_s()

elif section == "Derivative":
    direvative()

elif section == "Integration":
    solve_integrate()
