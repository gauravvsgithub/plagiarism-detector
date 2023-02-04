import streamlit as st
import computation as c


# sidebar
with st.sidebar:
    radio_res = st.radio(
        "Choose Algorithm",
        ("LCS", "No Idea")
    )

# page header
st.write(
    """
    # Plagiarism Detector
"""
)

st.write("##")


# tabs for evaluators and stdents
tab1, tab2 = st.tabs(["For Students", "For Evaluators"])

with tab1:
    st.header("For Students")
    with st.form("assignment_form"):
        st.write(
            """
    ## Submit the assignment
    """
        )
        mis_val = st.text_input("Enter MIS/ Roll Number")
        language = st.selectbox("Select programming language", ('C++', 'Java', 'Javascript', 'Python'))
        code = st.text_area("Enter Code", height=250)

        submitted = st.form_submit_button("Submit")
        if submitted:
            if(not mis_val or not code):
                st.error("Missing MIS or Code! Please enter all values.")
            else:
                c.submissions.append((mis_val, code))

            st.write(c.submissions)

with tab2:
    st.header("For Evaluators")
    score_pressed = st.button("Calculate Scores")
    if(score_pressed):
        message = c.compute_scores()
        if message!="Done!":
            st.error(message)
        else :
            st.success(message)
            st.write("""
                ## Scores
            """)
            c.compute_scores()
            st.table(c.getDataFrame())

