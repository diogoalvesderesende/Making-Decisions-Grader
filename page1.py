import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 1")
    st.write("""
    **How can Tentacle Tents ensure that their evaluation of marketing channels is comprehensive and not solely focused on immediate returns, taking into account long-term benefits and brand image?**
    """)

    # Initialize session state for Question 1 answer and feedback if not already set
    if 'answer_q1' not in st.session_state:
        st.session_state['answer_q1'] = ""
        
    if 'feedback_q1' not in st.session_state:
        st.session_state['feedback_q1'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q1'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q1'] = answer

        # Get feedback from the AI agent and save it to session state
        feedback = get_feedback(answer, 1)
        st.session_state['feedback_q1'] = feedback

        # Display the feedback
        st.write("**AI Feedback:**")
        st.write(feedback)

    # If feedback was already generated earlier, display it again
    if st.session_state['feedback_q1']:
        st.write("**Previous AI Feedback:**")
        st.write(st.session_state['feedback_q1'])
