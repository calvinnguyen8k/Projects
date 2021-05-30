"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the about page in the app.py file"""
    st.title("Calvin Nguyen Viet Cuong")
    st.markdown(
            """### Who Am I?

A Data Scientist with 8 years of experience in solving Business Problems, 
a constant learner and a firm believer of experimentation over expertise. 
Always on the lookout for new technologies, I am passionate about designing Data driven solutions which are easy, economical and can be scaled.\n

Besides that, Im also working across key functional business areas to driving global, multimillion-dollar growth; gains in customer retention; and record-setting profit improvements.
 
**Regional Data Science Lead | Business Analytics | Project Management | Microsoft Certified - Azure Data Scientist Associate**

[**LinkedIn**](https://www.linkedin.com/in/calvinnguyen8k/) | [**Email**](mailto:calvinnguyen8k@gmail.com)


""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
