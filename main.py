import pandas as pd
import os


input_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')

output_path = os.path.join(os.path.dirname(__file__), 'cleaned_sales_data.csv')

df = pd.read_csv(input_path)

df = df.drop_duplicates(subset="order_id")

df = df[df["total_price"] <= 800]

df = df[df["product_list"].notna()]

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df[df["order_date"].notna()]

df.to_csv(output_path, index=False)
