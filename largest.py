import streamlit as st

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


st.title("Find the Largest Among 3 Numbers")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")


if st.button("Find Largest"):
    result = find_largest(a, b, c)
    st.write("The largest number is:", result)
