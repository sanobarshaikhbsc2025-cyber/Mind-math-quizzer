import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Mind Math Quizzer",
    page_icon="🧠",
    layout="wide"
)

def generate_question():
    """Generates a new random math problem (+, -, *, /)."""
    ops = ['+', '-', '*', '/']
    op = random.choice(ops)

    if op == '+':
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
        question = f"What is {num1} + {num2}?"
        correct_answer = num1 + num2
    elif op == '-':
        num1 = random.randint(20, 100)
        num2 = random.randint(10, num1)
        question = f"What is {num1} - {num2}?"
        correct_answer = num1 - num2
    elif op == '*':
        num1 = random.randint(2, 12)
        num2 = random.randint(2, 12)
        question = f"What is {num1} * {num2}?"
        correct_answer = num1 * num2
    elif op == '/':
        divisor = random.randint(2, 10)
        answer = random.randint(2, 10)
        dividend = divisor * answer
        question = f"What is {dividend} / {divisor}?"
        correct_answer = answer
        
    return question, correct_answer

def on_next_question():
    """Callback function to handle 'Next Question' button click."""
    st.session_state.question_number += 1
    st.session_state.question, st.session_state.answer = generate_question()
    if 'user_input' in st.session_state:
        st.session_state.user_input = ""

def restart_game():
    """Callback function to reset the game state."""
    st.session_state.score = 0
    st.session_state.question_number = 1
    # Generate the first question directly
    st.session_state.question, st.session_state.answer = generate_question()
    if 'user_input' in st.session_state:
        st.session_state.user_input = ""


if 'score' not in st.session_state:
    restart_game()
 

st.markdown('<h1 style="color: black;">Mind Math Quizzer</h1>', unsafe_allow_html=True)


if st.session_state.question_number <= 10:
    st.write(f"Question: {st.session_state.question_number} / 10")
    st.write(f"Score: {st.session_state.score}")
    st.markdown(f'<h2 style="color: navy;">{st.session_state.question}</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 20px; color: skyblue;">Your answer:</p>', unsafe_allow_html=True)
    user_answer = st.text_input("Your answer:", label_visibility="hidden", key="user_input")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit"):
            try:
                user_answer_int = int(user_answer)
                if user_answer_int == st.session_state.answer:
                    st.success("Correct! 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"Wrong! 😟 The correct answer was {st.session_state.answer}")
            except ValueError:
                st.warning("Please enter a valid number.")

    with col2:
        st.button("Next Question", on_click=on_next_question)

else:
    # --- GAME OVER SCREEN ---
    st.balloons()
    st.header("🎉 Game Over! 🎉")
    st.write(f"**Your Final Score: {st.session_state.score} / 10**")
    st.button("Restart Quiz", on_click=restart_game)
