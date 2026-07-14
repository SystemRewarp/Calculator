import streamlit as st

st.title("Calculator")
st.write("---")

# Store the current number/expression
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display current expression
st.text_input("Display", value=st.session_state.expression, disabled=True)

# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    cols = st.columns(4)

    for i, button in enumerate(row):
        if cols[i].button(button):
            if button == "C":
                st.session_state.expression = ""

            elif button == "=":
                try:
                    result = eval(st.session_state.expression)
                    st.session_state.expression = str(result)
                except:
                    st.session_state.expression = "Error"

            else:
                st.session_state.expression += button

# Update display
st.text_input(
    "Result",
    value=st.session_state.expression,
    disabled=True
)
