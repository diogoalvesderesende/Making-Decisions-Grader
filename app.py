import streamlit as st

st.set_page_config(page_title="Tentacle Tents Decision-Making Case Study", layout="wide")

# Initialize session state variables for answers if they are not already initialized
for i in range(1, 6):
    if f'answer_q{i}' not in st.session_state:
        st.session_state[f'answer_q{i}'] = ""  # Default empty answer

# Function to save the current answer to session state
def save_answer(question_number, answer):
    st.session_state[f'answer_q{question_number}'] = answer

# Define functions for each question page
def question_1():
    st.title("Question 1")
    st.write("How can Tentacle Tents ensure that their evaluation of marketing channels is comprehensive and not solely focused on immediate returns, taking into account long-term benefits and brand image?")
    answer = st.text_area("Your answer:", st.session_state['answer_q1'])
    if st.button("Submit"):
        save_answer(1, answer)
        st.success("Answer submitted successfully!")

def question_2():
    st.title("Question 2")
    st.write("How might Monika Prpic's intuition affect her decision-making process in determining the most effective marketing channels?")
    answer = st.text_area("Your answer:", st.session_state['answer_q2'])
    if st.button("Submit"):
        save_answer(2, answer)
        st.success("Answer submitted successfully!")

def question_3():
    st.title("Question 3")
    st.write("What strategies could Tentacle Tents employ to avoid becoming overly committed to past decisions or investments that may not be yielding the desired results?")
    answer = st.text_area("Your answer:", st.session_state['answer_q3'])
    if st.button("Submit"):
        save_answer(3, answer)
        st.success("Answer submitted successfully!")

def question_4():
    st.title("Question 4")
    st.write("What factors should Tentacle Tents consider in their evaluation of what would be effective for their own brand, and how can they maintain an independent perspective?")
    answer = st.text_area("Your answer:", st.session_state['answer_q4'])
    if st.button("Submit"):
        save_answer(4, answer)
        st.success("Answer submitted successfully!")

def question_5():
    st.title("Question 5")
    st.write("How can Tentacle Tents ensure that their decision-making process takes into account the perspectives and preferences of different customer segments, without overemphasizing one particular group?")
    answer = st.text_area("Your answer:", st.session_state['answer_q5'])
    if st.button("Submit"):
        save_answer(5, answer)
        st.success("Answer submitted successfully!")

# Dictionary mapping page names to their respective question functions
PAGES = {
    "Question 1": question_1,
    "Question 2": question_2,
    "Question 3": question_3,
    "Question 4": question_4,
    "Question 5": question_5,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Dynamically call the selected page function
page_function = PAGES[selection]
page_function()

# Optionally: Provide a button to show all saved answers
if st.sidebar.button("Show All Saved Answers"):
    st.write("### Your Saved Answers:")
    for i in range(1, 6):
        st.write(f"**Question {i}:** {st.session_state[f'answer_q{i}']}")
