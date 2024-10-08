#!/usr/bin/python3

import pandas as pd
import sys

# Read the 'MegaMart_sales.csv' and 'MegaMart_newsales.csv' files
sales_df = pd.read_csv("MegaMart_sales.csv")
newsales_df = pd.read_csv("MegaMart_newsales.csv")

# Combine the two DataFrames
combined_df = pd.concat([sales_df, newsales_df], axis=0, ignore_index=True)

# Calculate the total sales value of the 'Office Supplies' category
office_supplies_sales = combined_df[combined_df['Category'] == 'Office Supplies']['Sales'].sum()
print(f"Total sales for 'Office Supplies': {office_supplies_sales}")

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('MegaMart_Combined_Sales.csv', index=False)
print("DataFrames have been combined and saved to 'MegaMart_Combined_Sales.csv'")

sys.exit()  # Proper exit of the script
