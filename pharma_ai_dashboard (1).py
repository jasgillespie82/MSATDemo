import streamlit as st
import pandas as pd

# Mock data for batch records
batch_data = pd.DataFrame({
    "Batch ID": ["B001", "B002", "B003", "B004"],
    "Yield (%)": [98.5, 95.2, 89.7, 92.3],
    "Deviation Notes": ["None", "Temperature spike", "Late material", "None"]
})

# Mock data for deviation analysis
deviation_data = pd.DataFrame({
    "Batch ID": ["B002", "B003"],
    "Issue": ["Temperature spike", "Late material"],
    "Severity": ["Medium", "High"]
})

# Mock data for predictive maintenance
maintenance_data = pd.DataFrame({
    "Equipment": ["Mixer A", "Dryer B", "Pump C"],
    "Predicted Issue": ["Bearing wear", "Overheating", "Seal leak"],
    "Risk Level": ["High", "Medium", "Low"]
})

# Streamlit app layout
st.title("AI in Pharma Operations Dashboard")

# Sidebar navigation
option = st.sidebar.selectbox("Select Use Case", [
    "Batch Record Review",
    "Deviation Analysis",
    "Predictive Maintenance"
])

# Display selected use case
if option == "Batch Record Review":
    st.header("Batch Record Review")
    st.write("Review batch performance and identify deviations.")
    st.dataframe(batch_data)

elif option == "Deviation Analysis":
    st.header("Deviation Analysis")
    st.write("Analyze batches with recorded deviations.")
    st.dataframe(deviation_data)

elif option == "Predictive Maintenance":
    st.header("Predictive Maintenance")
    st.write("Monitor equipment and predict potential failures.")
    st.dataframe(maintenance_data)
