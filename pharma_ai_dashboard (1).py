Streamlit.

How to use Streamlit in 3 seconds:

    1. Write an app
    >>> import streamlit as st
    >>> st.write(anything_you_want)

    2. Run your app
    $ streamlit run my_script.py

    3. Use your app
    A new tab will open on your browser. That's your Streamlit app!

    4. Modify your code, save it, and watch changes live on your browser.

Take a look at the other commands in this module to find out what else
Streamlit can do:

    >>> dir(streamlit)

Or try running our "Hello World":

    $ streamlit hello

For more detailed info, see https://docs.streamlit.io.

import streamlit as st
import pandas as pd

batch_data = pd.DataFrame({
    'Batch ID': ['B001', 'B002', 'B003', 'B004'],
    'Status': ['Complete', 'Deviation', 'Complete', 'Deviation'],
    'Yield (%)': [98.5, 92.3, 97.8, 89.4],
    'Deviation Notes': ['None', 'Temperature spike', 'None', 'Incorrect mixing time']
})

maintenance_data = pd.DataFrame({
    'Machine': ['Mixer A', 'Filler B', 'Labeler C'],
    'Last Maintenance': ['2025-09-15', '2025-08-30', '2025-10-01'],
    'Predicted Issue': ['Bearing wear', 'Valve clog', 'Sensor drift'],
    'Risk Level': ['Medium', 'High', 'Low']
})

st.title("AI in Pharma Operations Dashboard")

st.header("Batch Record Review")
st.dataframe(batch_data)

deviation_batches = batch_data[batch_data['Status'] == 'Deviation']
st.subheader("Deviation Analysis")
st.write("Batches with deviations:")
st.dataframe(deviation_batches)

st.header("Predictive Maintenance Insights")
st.dataframe(maintenance_data)

high_risk = maintenance_data[maintenance_data['Risk Level'] == 'High']
st.subheader("High Risk Equipment")
st.write("Machines requiring urgent attention:")
st.dataframe(high_risk)
