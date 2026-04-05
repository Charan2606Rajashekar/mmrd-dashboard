import streamlit as st

st.title("Mexican Fintech Readiness Dashboard")
st.write("MMRD - Testing Version")

st.header("About This Dashboard")
st.write("""
This dashboard measures fintech readiness across 32 Mexican states.

Four dimensions measured:
- Supply: Banking infrastructure
- Demand: Financial behavior
- Digital: Technology access
- Barriers: Socioeconomic obstacles
""")

st.header("Pages")
st.write("""
1. Choropleth - Geographic map showing FRI scores
2. Comparison - Compare states
3. Decomposition - Break down scores
4. Analysis - Statistical validation
""")

st.write("---")
st.write("Testing Version - Dummy Data")