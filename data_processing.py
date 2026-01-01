import pandas as pd

# -------------------------------
# STEP 1: Load all three CSV files
# -------------------------------
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# -------------------------------
# STEP 2: Combine into one DataFrame
# -------------------------------
combined_df = pd.concat([df0, df1, df2], ignore_index=True)

# -------------------------------
# STEP 3: Filter only Pink Morsels
# -------------------------------
pink_df = combined_df[
    combined_df["product"].str.contains("pink", case=False, na=False)
].copy()

# -------------------------------
# STEP 4: Clean price column
# Remove $ sign and convert to float
# -------------------------------
pink_df["price"] = (
    pink_df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

# -------------------------------
# STEP 5: Create sales column
# sales = quantity * price
# -------------------------------
pink_df["sales"] = pink_df["quantity"] * pink_df["price"]

# -------------------------------
# STEP 6: Keep only required columns
# -------------------------------
final_df = pink_df[["sales", "date", "region"]]

# -------------------------------
# STEP 7: Save processed output
# -------------------------------
final_df.to_csv("data/processed_sales_data.csv", index=False)

# -------------------------------
# STEP 8: Verification
# -------------------------------
print("Data processing complete.")
print("Rows written:", len(final_df))
print(final_df.head())
