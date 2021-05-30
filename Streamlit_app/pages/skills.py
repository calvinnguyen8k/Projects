"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Skills :hammer_and_wrench:")
    st.markdown(
            """## Languages

- Python
- SQL 
- VBA
- R
- JavaScript
## Platforms and Libraries

- **MS Office** - Excel, Powerpoint, Project, Word
- **Python** - Pandas, Numpy, Skicit Learn,Scipy, NLTK, Tensorflow, Keras, Streamlit, Dash, Plotly, Matplotlib, Seaborn, Flask, etc.
- **R** - Shiny, Dplyr
- **SQL** - MS SQL, MySQL, PostgreSQL, Redshift, Hive, Presto
- JavaScript  
- Tableau
- PowerBI
- JIRA, Confluence

## Analytical Skills
- Statistical Data Analysis
- Data Wrangling
- Hypothesis Testing
- Machine Learning
- Natural Language Processing
- Web Scraping

## Azure Stack
- Machine Learning
- MS SQL
- Synapse Analytics
- App Service
- Data Factories
- Virtual Machine
- Databricks
- Azure Directory
- Kubernetes Service
- Data Lake Storage 

## AWS Stack
- EC2
- S3
- RDS - Redshift

            




""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
