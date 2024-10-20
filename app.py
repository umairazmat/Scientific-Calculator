import streamlit as st


# Define the calculator functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Streamlit app title
st.title("Calculator")
st.write("This is a simple calculator app.")
st.write(
    "Enter two numbers and select the operation from the dropdown to perform the calculation."
)

# Dropdown to select the operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Input fields to take two numbers from the user
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Calculate based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {num1} / {num2} = {result}")
