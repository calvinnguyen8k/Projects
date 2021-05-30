"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Experience")
    st.markdown(
            """## GRAB

A multinational technology company headquartered in Singapore. Operating in transportation, delivery, and digital
payment services via the mobile app
        
            
### Regional Data Science Lead - Analytics | Dec 2018 – Present 
- Measures effectiveness of improvements through deep analysis and deliver end-to-end solutions such as estimating product impact seizing, instrumentation, experiment design, A/B
testing, improving data quality, and execution to deliver the product to the market
- Working closely with leadership in Engineering and Product Management to establish database structures, data models, and new products that enhance client insight
- Developing key metrics and performance indicators to evaluate overall financial performance
- Dive into large, noisy, and complex real-world behavioral data to produce an innovative analysis of historical patterns in customer behaviors and product performance
- Integration of data sources and the development of data routines to create information from raw data sources
- Working closely with data warehouse architects and software developers to generate seamless business intelligence solutions for business partners
- Build and deploy Auto Retention Exploratory System (A.R.E.S) webapp which is serving transport, food, delivery, financial team to explore factors influencing customer retention
- Leading and developing demand analytics teams across South East Asia

**Achievement**

- Owned a patent which has been approved by Grab Patent Review Board with the highest score
- 450k subscription sold regionally and drove $1M/monthly incremental revenue
- Transport revenue increase 17% and Food revenue increase 14% across the region
- Create a self-service data platform and monitor Tableau dashboard which reduce 32k$ data
extract cost per month
            
### Country Data Analytics Manager | Jul 2017 - Aug 2018
- Utilizing a hypothesis-driven problem-solving approach to design, construct, and test/iterate exploratory analyses that will reveal insight and opportunities for business users
- Communication, presentation, and delivering messages with impact to business stakeholder by translate technical information to a non-technical audience
- Analyzing data to understand user behavior and identify opportunities to optimize promotion/incentive programs to reduce cost and increase profit through AB testing
- Working with large datasets and distributed computing tools (Hive, Presto, etc.)
- Leading and developing country analytics team

**Achievement**

- Supply Segmentation, Monitoring, Churn Prediction, AB Test Experiment which contributed to
10% revenue increment and 16.5% of cost reduction at country level
- Vietnam became the first country in the region that has a positive profit
- Achieved 80% market share for Grab-Bike and 70% Grab-Car in Vietnam

### Senior Business Intelligence and Analytics Consultant | Jun 2016 - Jun 2017
- Designing market/business intelligence reports and performance measurement dashboards
- Building analytics solutions using varieties of big data technologies and create robust documentation of solutions and underlying design
- Collaborating with various expert teams to rollout effective products/services and to expand Grab’s universe of data for building richer insights

**Achievement**

- Completed market insight analytics which saved 14% incentive cost
- Used Tableau to track and analyze driver performance
- Create automation tool which helps to auto-download, calculate and send daily report to
stakeholder

## TOLUNA
A multinational company headquartered in France which provided real-time insights at the speed of the
on-demand economy. Global-scale, innovative technology, and research design

### Data Science Manager | Sep 2018 - Dec 2018
- Providing efficient data analytic to drive for optimized resource allocation, better decision making, and performance management
- Providing strategic direction and takes accountability for requirements, procedures, and standards
- Leading Data Science team across Singapore, Malaysia, Hongkong

**Achievement**

- Generating insight, actionable and recommendation meet 90% external client expectation

## LAZADA
A multinational technology company headquartered in Singapore that focuses mainly on e-commerce

### Regional Data Analytics Lead | Nov 2015 - Jun 2016
- Performing research and analysis to support business operations, develop recommendations to address problems/issues, and make presentations to managers and key stakeholders.
- Working closely with management on important issues and projects. Assess and document existing business procedures.
- Developing recommendations for new methods/procedures, implementation plans, schedules, and written reports for management to evaluate
- Identifying approaches to improve the accuracy and effectiveness of analytics models
- Leading and growth regional analytics team across South East Asia

**Achievement**
- Providing investor report with 100% accuracy to C-level
- Created auto multi source tool which auto classify over 30,000 products to 20 categories based on its name and description
- Recruit, train, and grow regional analytics team from 1 to 5 people

### Regional Senior Data Analytics | Nov 2014 - Nov 2015
- Providing management reports to support operation objects and commitments.
- Building data pipelines and interfaces to process complex datasets and translate them into actionable insights

**Achievement**
- Developed Key Item Performance which gave the sale team have a visibility on the top sale
item
- Developed Warehouse and Sourcing Performance to monitors sourcing and warehouse which help warehouse team decrease 30% of the time in the process from picking to shipping an item

### Regional Data Analytics | Oct 2013 - Nov 2014
- Responsible for data management, reporting, and analysis for the region (South East Asia)
- Analyzing and exploit opportunities to improve the customer experience from an operations perspective

**Achievement**

- Use MySQL to extract data from multi-source and provided synthetic analysis on excel to served multi-purpose business stakeholder
""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
