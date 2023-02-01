import streamlit as st

st.write(
    """
    # Plagiarism Detector
"""
)

st.write("##")

submissions = dict()

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
            submissions[mis_val] = code

            
            
        st.write(submissions)

