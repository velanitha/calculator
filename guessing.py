import streamlit as st
import random

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)


st.title("Guess the Number Game")

guess = st.number_input("Guess a number between 1 and 100", min_value=1, max_value=100, step=1)

if guess:
    if guess < st.session_state.number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Correct! The number was {st.session_state.number}.")
        # Reset game after correct guess
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
