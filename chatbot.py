import streamlit as st 

# st.header("Welcome to the chatbot application")
# st.write("message here ")
# st.text("texts")
# st.write(["shubham","shivam","sahil"])
# #st.button("Click Me")
# if st.button("click Me"):
#     st.write("Button Clicked")
    
# st.text_input("Enter your message here")

# st.header("chatbot")

# prompt = st.chat_input("enter your prompt")

# if prompt:
#     st.write(prompt)
    
# with st.sidebar:
#     st.header("this is header")
#     st.write("this is write")
#     st.button("this is button")
    
# st.markdown(
#     "<p style ='color:green;'> Application is running! </p>",
#     unsafe_allow_html = True
#     )

import streamlit as st

st.title("🧮 Simple Calculator")

# Take numbers from user
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2

    # Display result
    if not (operation == "Division" and num2 == 0):
        st.success(f"Result = {result}")