import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Social Media Engagement Analysis")

st.title("📊 Social Media Engagement Analysis")

# Load data
data = pd.read_csv("synthetic_social_media_data.csv")

st.header("Dataset Preview")
st.dataframe(data.head())

# Sidebar filters
st.sidebar.header("Filters")

post_type = st.sidebar.selectbox(
    "Select Post Type",
    data["Post_Type"].dropna().unique()
)

filtered_data = data[data["Post_Type"] == post_type]

st.subheader(f"Posts of type: {post_type}")
st.dataframe(filtered_data.head())

# Engagement distribution
st.subheader("Engagement Distribution")

fig, ax = plt.subplots()
sns.countplot(x="Engagement_Level", data=data, ax=ax)
st.pyplot(fig)

# Correlation heatmap
st.subheader("Feature Correlation")

num_data = data.select_dtypes(include=["float64", "int64"])

fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(num_data.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Feature vs engagement
st.subheader("Feature vs Engagement")

feature = st.selectbox("Select Feature", num_data.columns)

fig, ax = plt.subplots()
sns.boxplot(x="Engagement_Level", y=feature, data=data, ax=ax)
st.pyplot(fig)