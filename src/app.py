
from typing_extensions import ReadOnly
import streamlit as st
from streamlit_ace import st_ace
from engine import run_code
from submission import submissions, Submission
import os

# To handle page navigation between problem details and submission
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # default page

def navigate_to_submit():
    st.session_state.page = 'submit'

def navigate_to_home():
    st.session_state.page = 'home'

def get_Task_names():
    try:
        path = os.path.join(os.getcwd(), 'assets', 'problems')
        elements = os.listdir(path)
        folder_names = [element for element in elements if os.path.isdir(os.path.join(path, element))]
        
        return folder_names
    except OSError as e:
        print(f"error: {e}")
        return None

def get_problem_description(problem_name):
    try:
        problem_path = os.path.join(os.getcwd(), 'assets', 'problems', problem_name, 'description.txt')
        with open(problem_path, 'r') as f:
            description = f.read()
        return description
    except OSError as e:
        print(f"Error loading problem description: {e}")
        return "Problem description not available."
    

def display_verdicts(verdicts: str | list[str]):
    if verdicts == "CE":
        st.error("Compilation Error")
    else:
        for idx, verdict in enumerate(verdicts):
            if verdict == "AC":
                st.success(f"Testcase {idx + 1}: {verdict}")
            else:
                st.error(f"Testcase {idx + 1}: {verdict}")

tasks = get_Task_names()

if st.session_state.page == 'home':
    st.title("Available Problems")

    for title in tasks:
        st.write(f"### {title}")
        if st.button(f"Open Task {title}"):
            st.session_state.selected_task = title
            st.session_state.page = 'problem_details'

elif st.session_state.page == 'problem_details':
    problem_name = st.session_state.selected_task
    st.title(f"Problem: {problem_name}")
    
    # Show problem description
    description = get_problem_description(problem_name)
    st.write(description)
    
    # Button to navigate to submit page
    if st.button("Submit Code"):
        navigate_to_submit()

elif st.session_state.page == 'submit':
    st.title("Submit Your Code")
    
    code = st_ace(
        "Your code goes here...",
        language="python",
        font_size=13,
        theme="chrome",
        readonly=False,
        auto_update=True,
    )
    
    if st.button("Submit"):
        st.write("Submitted")
        st.code(code, language='python')

        # Simulating problem path for now, assuming it will be properly assigned during testing.
        verdicts = run_code(code, problem_path="example_problem")
        submissions.append(Submission(code, verdicts))
        display_verdicts(verdicts)

    if len(submissions) != 0:
        st.write("Submissions")
    for i, submission in list(enumerate(submissions))[::-1]:
        with st.expander(f"Submission #{i + 1} -------- {submission.time.strftime('%B %d, %Y, %I:%M:%S')}"):
            st_ace(submission.source_code, key=i, language="python", font_size=11, theme="chrome", readonly=True, auto_update=True)
            display_verdicts(submission.verdicts)
    
    if st.button("Back to Problems"):
        navigate_to_home()
