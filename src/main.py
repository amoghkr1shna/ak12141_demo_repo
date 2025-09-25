import math  # unused import (ruff will complain)

import streamlit as st


def add(a: int, b: int) -> int: 
    return a + b


st.title("OSource Demo App")  # inconsistent quotation marks (ruff will fix)

name = st.text_input("Enter your name")  # spacing issue around =

if name != "":
    st.write(f"Hello {name}!")  # bad indentation + spacing

number = st.number_input("Pick a number", min_value=0, max_value=100, value=10)

if st.button("Square it"):
    st.write("Square is:", math.pow(number, 2))  # missing space after colon