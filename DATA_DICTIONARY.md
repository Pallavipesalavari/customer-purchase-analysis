# Data Dictionary

The dashboard expects a CSV file with the following columns.

| Column | Type | Description | Example |
|---|---|---|---|
| `Customer_ID` | Text | Unique identifier used to group a customer | `101` |
| `Customer_Name` | Text | Customer's display name | `Ravi` |
| `Product` | Text | Purchased product name | `Laptop` |
| `Quantity` | Number | Number of units in the transaction | `2` |
| `Price` | Number | Price per unit, in the dataset's currency | `15000` |

## Calculated field

`Total_Amount` is calculated by the Streamlit app:

`Total_Amount = Quantity × Price`

The CSV upload must contain all five input columns. The app creates `Total_Amount`
during processing; it should not be supplied as a required input column.
