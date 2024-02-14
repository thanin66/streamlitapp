import streamlit as st

def calculator():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number:")
    operation = st.selectbox("Select operation:", ["+", "-"])
    num2 = st.number_input("Enter the second number:")

    result = 0
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2

    st.write("Result:", result)

if __name__ == "__main__":
    calculator()
