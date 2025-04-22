import streamlit as st

st.set_page_config(page_title="Guess the Number", page_icon=":moyai:",layout="centered")
st.title("Guess the Number Game")
st.write("***Think of a number between 1 and 10.*** Let's see if I can guess it!")

# Question sets
questions = {
    "Q1": [10, 7, 1, 6, 5],
    "Q2": [10, 4, 8, 5],
    "Q3": [10, 2, 4, 7],
    "Q4": [2, 3, 5, 10, 9, 1, 4, 7],
    "Q5": [10, 2, 4, 7, 9]
}

# Result mapping
mapping = {
    10: 6, 20: 8, 30: 3, 40: 1, 50: 9,
    60: 5, 70: 2, 80: 7, 90: 4, 100: 10
}

# Initialize state
if "step" not in st.session_state:
    st.session_state.step = 1
if "result" not in st.session_state:
    st.session_state.result = 0

# Function to go to next step
def next_step(add_points):
    points = [10, 20, 20, 30, 20]
    if add_points:
        st.session_state.result += points[st.session_state.step - 1]
    st.session_state.step += 1
    st.rerun()  # Rerun immediately to reflect changes

# Main game flow
step = st.session_state.step
if step <= 5:
    st.subheader(f"Question {step}")
    q_key = f"Q{step}"
    st.write("Is your number in this list?")
    st.code(", ".join(map(str, questions[q_key])), language="text")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            next_step(True)
    with col2:
        if st.button("No"):
            next_step(False)

elif step > 5:
    num = mapping.get(st.session_state.result, None)
    if num:
        st.success(f"*The number you thought is: {num}*")
        st.balloons()
    else:
        st.error("Hmm, something went wrong. Please restart the game.")

    if st.button("Restart Game"):
        st.session_state.step = 1
        st.session_state.result = 0
        st.rerun()