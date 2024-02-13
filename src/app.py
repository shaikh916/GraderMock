import streamlit as st 
from streamlit_ace import st_ace
from engine import run_code

code = st_ace( "Your code goes here...",
    language="python",
    font_size=13,
    theme="chrome",
    readonly=False,
    auto_update=True,
)

if st.button("Submit"):
    st.write("Submitted")
    st.code(code, language='python')

    verdicts = run_code(code, problem_path="example_problem")

    for idx, verdict in enumerate(verdicts):
        if verdict == "AC":
            st.success(f"Testcase {idx + 1}: {verdict}")
        else:
            st.error(f"Testcase {idx + 1}: {verdict}")