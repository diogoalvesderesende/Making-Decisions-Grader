import streamlit as st
from ai_agent import get_feedback

def app():
    st.title("Question 1")
    st.write("""
    **How can Tentacle Tents ensure that their evaluation of marketing channels is comprehensive and not solely focused on immediate returns, taking into account long-term benefits and brand image?**
    """)

    # Initialize the session state for Question 1 if not already set
    if 'answer_q1' not in st.session_state:
        st.session_state['answer_q1'] = ""  # Default empty value

    # Use the saved answer in session state, if available
    answer = st.text_area("Your answer:", value=st.session_state['answer_q1'], height=200)

    # If the user submits the answer
    if st.button("Submit"):
        # Save the answer to session state
        st.session_state['answer_q1'] = answer
        
        # Get feedback from the AI agent
        feedback = get_feedback(answer, 1)
        st.write("**AI Feedback:**")
        st.write(feedback)
