from typing import Text

import streamlit as st 
st.title("Calculator")
st.write('''
         1.addition
         2.subraction
         3.multiplication
         4.division''')
choice = st.number_input("Enter your choice:",value = 0)
num1 = st.number_input("Enter first number:",value = 0)
num2 = st.number_input("Enter second number",value = 0)
if st.button("click here"):
    if choice==1:
        st.write(num1 + num2)
    elif choice==2:
        st.write(num1 - num2)
    elif choice==3:
        st.write(num1 * num2)
    else:
        st.write(num1 / num2)
    