import streamlit as st
import computation as c
st.write(
    """
    # Plagiarism Detector
"""
)

st.write("##")

with st.form("assignment_form"):
    st.write(
        """
   ## Submit the assignment
   """
    )
    mis_val = st.text_input("Enter MIS/ Roll Number")
    code = st.text_area("Enter Code", height=500)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if(not mis_val or not code):
            st.error("Missing MIS or Code! Please enter all values.")
        else:
            c.submissions.append((mis_val, code))

            
            
        st.write(c.submissions)

score_pressed = st.button("Calculate Scores")
if(score_pressed):
    message = c.compute_scores()
    if message!="Done!":
        st.error(message)
    else :
        st.success(message)
        c.compute_scores()
        st.write(c.scores)
    
