# Testing Guide

## Before testing
Install the packages:

```bash
pip install -r requirements.txt
```

Start the dashboard:

```bash
streamlit run app.py
```

## Manual test cases

| Test | Action | Expected result |
|---|---|---|
| Default data | Open the app without uploading a file | Built-in sample transactions are displayed |
| Valid CSV | Upload `customer_purchases.csv` | Dataset and analysis sections are displayed |
| Missing column | Upload a CSV without one required column | An error lists the missing column |
| Invalid numeric value | Include text in `Quantity` or `Price` | The invalid row is excluded during cleaning |
| Negative value | Include a negative quantity or price | The negative-value row is excluded |
| Customer analysis | Review customer spending | Spending totals are grouped by customer |
| Product analysis | Review product quantities | Quantities are grouped by product |
| CSV download | Click the download button | A cleaned input dataset CSV is downloaded |

## Note
These are manual test instructions, not a claim that automated tests have been run.
