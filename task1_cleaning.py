import pandas as pd


df = pd.read_csv("data/sales_data.csv")

print("===== ORIGINAL DATA =====")
print(df.head())


print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print("Number of duplicates:", df.duplicated().sum())


df = df.drop_duplicates()


text_columns = ["Customer", "Product", "Category", "Region"]

for column in text_columns:
    df[column] = df[column].str.strip()

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Convert numeric columns
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"])

# Create Sales column
df["Sales"] = df["Quantity"] * df["Unit_Price"]

# Save cleaned dataset
df.to_csv("data/cleaned_sales_data.csv", index=False)

print("\n===== CLEANED DATA =====")
print(df.head())

print("\nCleaned dataset saved successfully!")