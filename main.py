import streamlit as st

st.title("Calculator")
st.write("---")

# Create expression if it doesn't exist
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display
st.text_input(
    "Display",
    value=st.session_state.expression,
    disabled=True
)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in buttons:
    cols = st.columns(4)

    for i, button in enumerate(row):
        if cols[i].button(button, use_container_width=True):

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

            # Refresh immediately so the display updates
            st.rerun()
