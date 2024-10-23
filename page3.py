import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 3")
    st.write("""
    **What strategies could Tentacle Tents employ to avoid becoming overly committed to past decisions or investments that may not be yielding the desired results?**
    """)

    # Initialize session state for Question 3 if not already set
    if 'answer_q3' not in st.session_state:
        st.session_state['answer_q3'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q3'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q3'] = answer

        # Get feedback from the AI agent
        feedback = get_feedback(answer, 3)
        st.write("**AI Feedback:**")
        st.write(feedback)
