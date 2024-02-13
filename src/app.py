import streamlit as st 
from engine import run_code

code = st.text_area(
    label = "Code to submit",
    value = "Put your code here in Python",
    height=300
)

if code != "Put your code here in Python":
    st.code(code, language='python')

    verdict = run_code(code, problem_path="example_problem")

    st.write(verdict)