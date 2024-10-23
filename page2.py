import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 2")
    st.write("""
    **How might Monika Prpic's intuition affect her decision-making process in determining the most effective marketing channels? What methods can be used to validate or complement intuitive decision-making?**
    """)

    # Initialize session state for Question 2 if not already set
    if 'answer_q2' not in st.session_state:
        st.session_state['answer_q2'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q2'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q2'] = answer

        # Get feedback from the AI agent
        feedback = get_feedback(answer, 2)
        st.write("**AI Feedback:**")
        st.write(feedback)
