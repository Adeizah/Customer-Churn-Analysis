# Customer-Churn-Analysis

## Overview

The **Customer Churn Analysis** project applies data analysis and visualization techniques to investigate customer churn in a telecom company. The primary objective is to understand the key factors contributing to customer attrition, estimate the financial impact of churn, and provide actionable insights for improving customer retention. The project leverages Python and Streamlit to analyze and present data, with a focus on customer demographics, service usage, and satisfaction.

### Key Insights:
- **Main Drivers of Churn:** The top reasons for churn include competitor offerings and customer dissatisfaction. Service support and contract type (long-term vs month-to-month) also play significant roles in customer retention.
- **Financial Impact:** Churned customers resulted in an estimated **$4.89M in lost revenue**.
- **Retention Strategies:** Providing tech support and offering long-term contracts are effective strategies to reduce churn.

An interactive **Streamlit dashboard** was developed to visualize the analysis and provide a user-friendly way for stakeholders to explore key metrics such as churn rates, total revenue loss, and factors influencing churn.

## Data

The dataset used in this project was obtained from **[Kaggle](https://www.kaggle.com)** at [**Telco Customer Churn**](https://www.kaggle.com/datasets/abdallahwagih/telco-customer-churn) It consists of customer data, including demographic information and details about their telecom subscriptions. The analysis focuses on the following key features:

- **Customer Demographics:** Age, gender, senior citizen status, and dependents.
- **Subscription Details:** Type of contract, payment method, and services used (e.g., internet, phone).
- **Churn Information:** Whether the customer has churned or not.

### Data Cleaning & Transformation

The data underwent several transformation steps to ensure consistency and usability:

- Removed unnecessary columns such as `Country`, `State`, `Zip Code`, and redundant location data (`Latitude`, `Longitude`).
- Converted `Total Charges` column from string to numeric values.
- Grouped churn reasons into broader categories to simplify analysis.

## Analysis & Insights

Through data analysis, several key insights were uncovered:

1. **Demographic Factors:** Senior citizens, customers without dependents, and those with month-to-month contracts exhibit higher churn rates.
2. **Service Usage & Churn:** Customers with fiber optic internet services tend to churn at higher rates than those using DSL. Similarly, customers who don't use tech support have a higher churn rate compared to those who do.
3. **Revenue Impact:** The analysis revealed a significant financial loss, with churned customers contributing to approximately **$4.89 million in lost revenue**. 
4. **Retention Strategies:** Offering long-term contracts and providing tech support are associated with lower churn rates. Customers on long-term contracts, in particular, are more likely to stay, reducing the risk of churn.

## Streamlit Dashboard

An interactive **Streamlit dashboard** was developed to allow users to explore the insights visually. The dashboard allows stakeholders to:

- Visualize churn rates across various customer segments.
- Track key performance indicators such as total churned customers, total expected revenue, and total revenue loss.
- Filter data to analyze the factors contributing to churn and explore different segments interactively.
