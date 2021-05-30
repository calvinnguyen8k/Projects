"""Edu page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Education :books:")
    st.markdown(
            """### Fachhochschule Nordwestschweiz
**MBA in Finance and Banking | 2011 - 2013** | [**FHNW**](https://www.fhnw.ch/)\n

### Ho Chi Minh City Open University
**Bachelor of Computer Science | 2004 - 2009** | [**OU**](https://ou.edu.vn/)

### Microsoft Certificate
** Azure Data Scientist Associate ** [Credential](https://www.credly.com/badges/7538f9ca-4289-4d1f-9687-a612eb544a07)
""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
