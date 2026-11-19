# 🛒 Customer Purchase Pattern Analysis
### An Interactive Data Analytics Dashboard Using Python, Streamlit & Apache Pig

<p align="center">
  **Transform Customer Transactions into Meaningful Business Insights!**
</p>

---

## 🌟 Project Overview

Customer Purchase Pattern Analysis is an interactive data analytics application designed to explore customer shopping behavior, analyze purchasing trends, and identify valuable business insights.

The application provides customer-wise spending analysis, product-wise purchase quantity analysis, interactive visualizations, and key performance metrics through a user-friendly Streamlit dashboard.

It also includes an Apache Pig Latin script demonstrating equivalent data analysis operations.

## ✨ Key Features

- 📊 **Interactive Dashboard** – Explore customer transactions through an attractive interface.
- 👥 **Customer Spending Analysis** – Identify the highest-spending customers.
- 🛍️ **Product Analysis** – Discover the most frequently purchased products.
- 📈 **Data Visualization** – Understand purchasing trends using charts.
- 📂 **CSV File Upload** – Analyze your own customer transaction datasets.
- 🔍 **Data Validation** – Check required columns and clean invalid numerical records.
- 💡 **Business Insights** – Automatically identify important purchase patterns.
- 📥 **CSV Download** – Download the current transaction dataset.
- 🐘 **Apache Pig Script** – Includes Pig Latin logic for customer and product analysis.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Streamlit | Web application |
| Pandas | Data processing |
| Apache Pig | Data analysis script |
| CSV | Dataset management |

## 📊 Dashboard Analysis

The application provides:

1. Customer Purchase Dataset
2. Customer-wise Total Spending
3. Product-wise Purchase Quantity
4. Key Business Findings
5. Downloadable Dataset

## 📁 Project Structure

```text
Customer-Purchase-Pattern-Analysis/
│
├── app.py
├── requirements.txt
├── README.md
├── customer_purchases.csv
├── customer_purchase_analysis.pig
│
├── PROJECT_OVERVIEW.md
├── DATA_DICTIONARY.md
├── METHODOLOGY.md
├── TESTING.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── .gitignore
```

## 🚀 Installation & Execution

### Option 1: Run Locally

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd Customer-Purchase-Pattern-Analysis
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the application**

```bash
streamlit run app.py
```

### Option 2: Deploy Online

1. Visit https://share.streamlit.io/
2. Sign in using your GitHub account.
3. Select your project repository.
4. Choose the appropriate branch.
5. Set the main file path to `app.py`.
6. Click Deploy.

## 📄 Dataset Requirements

Upload a CSV file containing the following columns:

```text
Customer_ID
Customer_Name
Product
Quantity
Price
```

The application calculates transaction amounts automatically using:

**Total Amount = Quantity × Price**

## 🎯 Project Objectives

- Analyze customer purchasing behavior.
- Calculate individual customer spending.
- Identify popular products.
- Present useful insights through visualizations.
- Demonstrate data processing using Python and Apache Pig concepts.

## 🔮 Future Enhancements

- Customer segmentation using Machine Learning.
- Purchase trend prediction.
- Interactive filtering by product and customer.
- Monthly and yearly sales analysis.
- Advanced business intelligence visualizations.
- Database integration.

## 👩‍💻 Developed By

**Pallavi Pesalavari**

B.Tech – Computer Science and Engineering (Data Science)

Madanapalle Institute of Technology and Science (MITS)


