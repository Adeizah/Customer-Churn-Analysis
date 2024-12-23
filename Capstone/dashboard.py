# Importing libraries
import streamlit as st
from millify import millify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
@st.cache_data  # Cache the data to improve performance
def load_data():
    data = pd.read_csv('./Capstone/Datasets/cleaned_churn_data.csv')
    return data

data = load_data()

# Title and Introduction
st.title("Customer Churn Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
contract_type = st.sidebar.multiselect(
    "Select Contract Type:",
    options=data['Contract'].unique(),
    default=data['Contract'].unique()
)
payment_method = st.sidebar.selectbox(
    "Select Payment Method:",
    options=data['Payment Method'].unique()
)

# Filter data based on user selection
filtered_data = data[
    (data['Contract'].isin(contract_type)) &
    (data['Payment Method'] == payment_method)
]

# KPI Columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_customers = len(data)
    st.metric(label="Total Customers", value=f"{total_customers:,}")

with col2:
    total_churn_count = len(data[data['Churn Label'] == 'Yes'])
    st.metric(label="Total Churn Count", value=f"{total_churn_count:,}")

with col3:
    total_expected_revenue = data['CLTV'].sum()
    total_expected_revenue = millify(total_expected_revenue, precision=2)
    st.metric(label="Total Expected Revenue", value=f"${total_expected_revenue}")

with col4:
    total_revenue = data['Total Charges'].sum()
    total_revenue = millify(total_revenue, precision=2)
    st.metric(label="Total Revenue", value=f"${total_revenue}")

with col5:
    churned = data[data['Churn Label'] == 'Yes']
    average_cltv = (churned['CLTV'] - churned['Total Charges']).mean()
    estimated_loss = average_cltv * total_churn_count
    estimated_loss = millify(estimated_loss, precision=2)
    st.metric(label="Estimated Revenue Loss", value=f"${estimated_loss}")

# Visualizations
st.subheader("Visualizations")

col1, col2, col3 = st.columns(3)
# Churn Reasons
with col1:
    st.markdown("### Reasons for Churning")
    order = filtered_data['Churn Reason'].value_counts().index
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_data, x='Churn Reason', ax=ax, order=order)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=10, rotation=45, ha='right')
    st.pyplot(fig)

# Churn Count Plot
with col2:
    st.markdown("### Churn Count by Contract Type")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_data, x='Contract', hue='Churn Label', ax=ax)
    st.pyplot(fig)

with col3:
    st.markdown("### Churn Count by Internet Service Type")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_data, x='Internet Service', hue='Churn Label', ax=ax)
    st.pyplot(fig)

col1, col2 = st.columns(2)

# CLTV Distribution
with col1:
    st.markdown("### CLTV Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['CLTV'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# Monthly Charges vs Tenure Scatter Plot
with col2:
    st.markdown("### Monthly Charges vs Tenure")
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='Tenure Months', y='Monthly Charges', hue='Churn Label', ax=ax)
    st.pyplot(fig)

# Key Insights Section
st.subheader("Key Insights (Direct)")
st.markdown("""
The main reasons why customers leave are:
- **Competitors** offering more appealing services,
- **Dissatisfaction** with the services and related aspects
- Challenges with service **support** 
Other factors cited include price, extra charges, relocation and even death.
""")

st.subheader("Key Insights (Indirect)")
st.markdown("""
1. High churn rates are observed among customers with month-to-month contracts.
2. Customers with long-term contracts exhibit lower churn.
3. CLTV varies widely but churn is not strongly correlated with high or low values.
""")
