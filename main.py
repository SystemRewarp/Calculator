import streamlit as st

st.title('Calculator')
st.write('---')

num1 = st.number_input(label='Enter First Number')
num2 = st.number_input(label='Enter Second Number')

st.write('Operation')
operation = st.radio('Select an operation to perform',
                     ('Add', 'Subtract', 'Multiply', 'Divide'))
ans = 0
 
def calculate():
    if operation == 'Add':
        ans = num1 + num2
    elif operation == 'Subtract':
        ans = num1 - num2
    elif operation == 'Multiply':
        ans = num1 * num2
    elif operation=='Divide' and num2!=0:
        ans = num1 / num2
    else:
        st.warning('Division by 0 error. Please enter a non-zero number.')
        ans = 'Not defined'
 
    st.success(f"Answer = {ans}")

if st.button('Calculate result'):
    calculate()
    #code by AskPython