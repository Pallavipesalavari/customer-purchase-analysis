import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Purchase Pattern Analysis", page_icon="🛒", layout="wide")

st.title("🛒 Customer Purchase Pattern Analysis")
st.caption("A Streamlit dashboard using a sample customer transaction dataset")

st.info(
    "Academic note: This app performs the calculations with Python and pandas inside Streamlit. "
    "It demonstrates the same analysis goals as the Apache Pig project, but it does not execute "
    "Pig Latin, Hadoop, or MapReduce."
)

SAMPLE_DATA = [
    {"Customer_ID": "101", "Customer_Name": "Ravi", "Product": "Laptop", "Quantity": 1, "Price": 50000},
    {"Customer_ID": "102", "Customer_Name": "Pallavi", "Product": "Mobile", "Quantity": 2, "Price": 15000},
    {"Customer_ID": "103", "Customer_Name": "Suresh", "Product": "Headphones", "Quantity": 1, "Price": 2000},
    {"Customer_ID": "101", "Customer_Name": "Ravi", "Product": "Mouse", "Quantity": 2, "Price": 500},
    {"Customer_ID": "102", "Customer_Name": "Pallavi", "Product": "Laptop", "Quantity": 1, "Price": 50000},
    {"Customer_ID": "104", "Customer_Name": "Anil", "Product": "Mobile", "Quantity": 1, "Price": 15000},
    {"Customer_ID": "103", "Customer_Name": "Suresh", "Product": "Keyboard", "Quantity": 1, "Price": 1500},
    {"Customer_ID": "101", "Customer_Name": "Ravi", "Product": "Headphones", "Quantity": 2, "Price": 2000},
]
REQUIRED = ["Customer_ID", "Customer_Name", "Product", "Quantity", "Price"]

st.sidebar.header("Choose dataset")
uploaded = st.sidebar.file_uploader("Upload a CSV file (optional)", type=["csv"])
if uploaded is not None:
    try:
        data = pd.read_csv(uploaded)
        missing = [c for c in REQUIRED if c not in data.columns]
        if missing:
            st.error("CSV is missing required columns: " + ", ".join(missing))
            st.stop()
        data = data[REQUIRED].copy()
    except Exception as exc:
        st.error(f"Could not read CSV: {exc}")
        st.stop()
else:
    data = pd.DataFrame(SAMPLE_DATA)

for col in ["Customer_ID", "Customer_Name", "Product"]:
    data[col] = data[col].astype(str)
for col in ["Quantity", "Price"]:
    data[col] = pd.to_numeric(data[col], errors="coerce")
data = data.dropna(subset=["Quantity", "Price"])
data = data[(data["Quantity"] >= 0) & (data["Price"] >= 0)].copy()
data["Quantity"] = data["Quantity"].astype(int)
data["Total_Amount"] = data["Quantity"] * data["Price"]

st.subheader("1. Customer purchase dataset")
st.dataframe(data[REQUIRED], use_container_width=True, hide_index=True)

c1, c2, c3 = st.columns(3)
c1.metric("Transactions", f"{len(data):,}")
c2.metric("Unique customers", f"{data['Customer_ID'].nunique():,}")
c3.metric("Unique products", f"{data['Product'].nunique():,}")

st.subheader("2. Customer-wise total spending")
customer_totals = (
    data.groupby(["Customer_ID", "Customer_Name"], as_index=False)["Total_Amount"]
    .sum()
    .sort_values("Total_Amount", ascending=False)
)
customer_totals = customer_totals.rename(columns={"Total_Amount": "Total_Spending"})
st.dataframe(customer_totals.style.format({"Total_Spending": "₹{:,.2f}"}), use_container_width=True, hide_index=True)
st.bar_chart(customer_totals.set_index("Customer_Name")["Total_Spending"])

st.subheader("3. Product-wise purchase quantity")
product_totals = (
    data.groupby("Product", as_index=False)["Quantity"]
    .sum()
    .sort_values(["Quantity", "Product"], ascending=[False, True])
    .rename(columns={"Quantity": "Total_Quantity"})
)
st.dataframe(product_totals, use_container_width=True, hide_index=True)
st.bar_chart(product_totals.set_index("Product")["Total_Quantity"])

st.subheader("4. Key findings")
if len(customer_totals):
    top_customer = customer_totals.iloc[0]
    st.success(
        f"Highest-spending customer: {top_customer['Customer_Name']} "
        f"(Customer ID {top_customer['Customer_ID']}) — ₹{top_customer['Total_Spending']:,.2f}."
    )
if len(product_totals):
    max_qty = product_totals["Total_Quantity"].max()
    top_products = product_totals.loc[product_totals["Total_Quantity"] == max_qty, "Product"].tolist()
    st.write(f"Most-purchased product(s): {', '.join(top_products)} — {int(max_qty)} units each.")

with st.expander("5. Apache Pig Latin logic for the report"):
    st.code("""purchases = LOAD 'customer_purchases.csv'
USING PigStorage(',')
AS (Customer_ID:chararray, Customer_Name:chararray,
    Product:chararray, Quantity:int, Price:double);

clean_data = FILTER purchases
BY Customer_ID != 'Customer_ID';

purchase_amount = FOREACH clean_data GENERATE
    Customer_ID, Customer_Name, Product, Quantity, Price,
    (Quantity * Price) AS Total_Amount;

grouped_data = GROUP purchase_amount
BY (Customer_ID, Customer_Name);

customer_totals = FOREACH grouped_data GENERATE
    group AS Customer,
    SUM(purchase_amount.Total_Amount) AS Total_Spending;

sorted_customers = ORDER customer_totals BY Total_Spending DESC;
DUMP sorted_customers;

product_group = GROUP clean_data BY Product;
product_analysis = FOREACH product_group GENERATE
    group AS Product_Name,
    SUM(clean_data.Quantity) AS Total_Quantity;

sorted_products = ORDER product_analysis BY Total_Quantity DESC;
DUMP sorted_products;""", language="pig")

csv_bytes = data[REQUIRED].to_csv(index=False).encode("utf-8")
st.download_button("Download current dataset as CSV", data=csv_bytes,
                   file_name="customer_purchases.csv", mime="text/csv")

st.caption("Sample-data results are illustrative. Replace the sample with your own CSV to analyze other transactions.")
