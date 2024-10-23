import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 4")
    st.write("""
    **What factors should Tentacle Tents consider in their evaluation of what would be effective for their own brand, and how can they maintain an independent perspective?**
    """)

    # Initialize session state for Question 4 answer and feedback if not already set
    if 'answer_q4' not in st.session_state:
        st.session_state['answer_q4'] = ""
        
    if 'feedback_q4' not in st.session_state:
        st.session_state['feedback_q4'] = ""

    # Use the saved answer if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q4'], height=200)

    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q4'] = answer

        # Get feedback from the AI agent and save it to session state
        feedback = get_feedback(answer, 4)
        st.session_state['feedback_q4'] = feedback

        # Display the feedback
        st.write("**AI Feedback:**")
        st.write(feedback)

    # If feedback was already generated earlier, display it again
    if st.session_state['feedback_q4']:
        st.write("**Previous AI Feedback:**")
        st.write(st.session_state['feedback_q4'])
