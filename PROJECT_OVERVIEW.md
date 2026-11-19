# Customer Purchase Pattern Analysis

## Project overview
This project analyzes customer transaction data and presents customer-wise spending,
product-wise purchase quantities, summary metrics, and key findings in a Streamlit dashboard.

## Included files
- `app.py` — Streamlit dashboard.
- `requirements.txt` — Python dependencies.
- `README.txt` — setup and deployment notes.
- `customer_purchases.csv` — sample dataset accepted by the dashboard.
- `customer_purchase_analysis.pig` — Apache Pig Latin example for customer and product analysis.
- `.gitignore` — excludes local environments, cache files, and secrets.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dataset format
The CSV must contain these columns:
`Customer_ID, Customer_Name, Product, Quantity, Price`

## Important note
The Streamlit dashboard uses Python and pandas. The `.pig` file is a separate Apache Pig
example and requires a compatible Pig/Hadoop environment; Streamlit does not execute it.
