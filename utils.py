import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to solve math problems
def solve_math_problem(problem, topic):
    try:
        messages = [
            {"role": "system", "content": f"You are an expert in {topic}."},
            {"role": "user", "content": f"Solve this problem step-by-step:\n{problem}"},
        ]
        response = client.chat.completions.create(
            messages=messages,
            model="gpt-4",
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Inject JavaScript to detect device width
st.markdown(
    """
    <script>
    const sendDeviceInfo = () => {
        const deviceWidth = window.innerWidth;
        const message = deviceWidth > 768 ? "desktop" : "mobile";
        window.parent.postMessage(message, "*");
    };
    sendDeviceInfo();
    window.addEventListener("resize", sendDeviceInfo);
    </script>
    """,
    unsafe_allow_html=True,
)

# Check the message sent by JavaScript
device = st.session_state.get("device", "desktop")

# Simulate receiving the message from JavaScript
if st.session_state.get("device") is None:
    st.session_state.device = "desktop"  # Default to desktop

# Show sidebar only on desktop
if st.session_state.device == "desktop":
    st.sidebar.title("Math Solver")

# App layout
st.title("Math Question Solver")
st.markdown("Enter a math problem below.")

topic = st.selectbox("Select a topic", ["Algebra", "Calculus", "Geometry", "Other"])
problem = st.text_area("Problem")

# Add a unique key to the button
if st.button("Solve", key="solve_button"):
    solution = solve_math_problem(problem, topic)
    st.text_area("Solution", solution, height=200)
