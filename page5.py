import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 5")
    st.write("""
    **How can Tentacle Tents ensure that their decision-making process takes into account the perspectives and preferences of different customer segments, without overemphasizing one particular group?**
    """)

    # Initialize session state for Question 5 if not already set
    if 'answer_q5' not in st.session_state:
        st.session_state['answer_q5'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q5'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q5'] = answer

        # Get feedback from the AI agent
        feedback = get_feedback(answer, 5)
        st.write("**AI Feedback:**")
        st.write(feedback)
