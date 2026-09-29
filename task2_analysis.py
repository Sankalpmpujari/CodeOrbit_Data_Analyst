import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sales_data.csv")

# Total Sales
total_sales = df["Sales"].sum()

# Total Orders
total_orders = df["Order_ID"].nunique()

# Average Order Value
average_order_value = total_sales / total_orders

# Top Products
top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Sales by Category
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Sales by Region
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("========== SALES ANALYSIS ==========")

print("\nTotal Sales:", total_sales)

print("Total Orders:", total_orders)

print("Average Order Value:", round(average_order_value, 2))

print("\n========== TOP PRODUCTS ==========")
print(top_products)

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

print("\n========== SALES BY REGION ==========")
print(region_sales)