import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Setup & Title
st.set_page_config(page_title="Marketing ROI Dashboard", layout="wide")
st.title("📊 Marketing Campaign Effectiveness Analyzer")
st.markdown(" Nixon Tse | Senior @ UCSB + The GOAT")

# 2. Load Data 
@st.cache_data
def load_data():
    # Make sure this filename matches your smaller file!
    df = pd.read_csv("data_small.csv")
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Results")
# Using 'Campaign_Type' as the filter based on your columns
campaign_type = st.sidebar.multiselect("Select Campaign Type:", 
                                       options=df['Campaign_Type'].unique(), 
                                       default=df['Campaign_Type'].unique())

# Filter the dataframe based on selection
mask = df['Campaign_Type'].isin(campaign_type)
df_filtered = df[mask]

# 4. Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("ROI by Channel")
    # Updated 'x' to 'Channel_Used' to match your data
    fig_roi = px.bar(df_filtered, x='Channel_Used', y='ROI', 
                     color='Channel_Used', title="Return on Investment per Channel")
    st.plotly_chart(fig_roi)

with col2:
    st.subheader("Conversion Rate vs. Acquisition Cost")
    # Updated 'x' to 'Acquisition_Cost' to match your data
    fig_scatter = px.scatter(df_filtered, x='Acquisition_Cost', y='Conversion_Rate', 
                             size='Clicks', color='Channel_Used', 
                             hover_name='Campaign_ID')
    st.plotly_chart(fig_scatter)

# 5. Business Insights
st.divider()
st.subheader("💡 Key Marketing Insights")
# Calculating which channel has the best average ROI
top_channel = df.groupby('Channel_Used')['ROI'].mean().idxmax()
st.write(f"The most effective channel for ROI in thipython3 -m streamlit run app.pys dataset was **{top_channel}**.")