import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 5")
    st.write("""
    **How can Tentacle Tents ensure that their decision-making process takes into account the perspectives and preferences of different customer segments, without overemphasizing one particular group?**
    """)

    # Initialize session state for Question 5 answer and feedback if not already set
    if 'answer_q5' not in st.session_state:
        st.session_state['answer_q5'] = ""
        
    if 'feedback_q5' not in st.session_state:
        st.session_state['feedback_q5'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q5'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q5'] = answer

        # Get feedback from the AI agent and save it to session state
        feedback = get_feedback(answer, 5)
        st.session_state['feedback_q5'] = feedback

        # Display the feedback
        st.write("**AI Feedback:**")
        st.write(feedback)

    # If feedback was already generated earlier, display it again
    if st.session_state['feedback_q5']:
        st.write("**Previous AI Feedback:**")
        st.write(st.session_state['feedback_q5'])
