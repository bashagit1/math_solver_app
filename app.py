import streamlit as st
from utils import solve_math_problem

# Streamlit App Title
st.title("Math Question & Problem Solver")

# Sidebar for topic selection
st.sidebar.title("Math Topics")
math_topic = st.sidebar.selectbox(
    "Select a topic",
    ["General Math", "Algebra", "Calculus", "Geometry", "Others"]
)

# Text area for user input
problem = st.text_area("Enter your math problem below:")

# Solve button
if st.button("Solve"):
    if problem.strip():
        # Call the OpenAI API through the helper function
        solution = solve_math_problem(problem, math_topic)
        # Display the solution
        st.subheader("Solution:")
        st.write(solution)
    else:
        st.error("Please enter a problem to solve!")
