import streamlit as st

st.set_page_config(page_title="MMRD Project", layout="wide")

st.title("Mexican Fintech Readiness Dashboard (MMRD)")
st.write("Welcome to my MSc Fintech research project dashboard.")

st.header("About This Project")
st.write("This dashboard measures the fintech readiness of all 32 Mexican states to identify areas of opportunity and infrastructure gaps.")
st.write("The Fintech Readiness Index (FRI) is calculated using a robust statistical pipeline (PCA weighting) based on four main dimensions:")

st.markdown("- **Supply:** Banking infrastructure (branches, ATMs)")
st.markdown("- **Demand:** Financial behavior (account ownership, transactions)")
st.markdown("- **Digital:** Technology access (internet, smartphone adoption)")
st.markdown("- **Barriers:** Socioeconomic obstacles (poverty, deprivation)")

st.header("Navigation")
st.write("Use the sidebar on the left to explore the dashboard:")
st.markdown("1. **Map:** View the geographic clustering of the FRI scores.")
st.markdown("2. **Comparison:** *(Coming soon)* Benchmark specific states against one another.")
st.markdown("3. **Decomposition:** *(Coming soon)* Analyze what is driving a specific state's score.")
st.markdown("4. **Diagnostics:** *(Coming soon)* View the statistical validation (KMO, PCA variance, Moran's I).")

st.write("---")
st.caption("Note: This version is currently using structural testing data. Real index scores will be updated here after running the main data pipeline.")
