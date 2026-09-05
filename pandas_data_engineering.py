## `pandas`

```
import pandas as pd

# ============================================================
# 1. CREATE DATAFRAME
# ============================================================

df = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["John", "Mary", "David", "Sarah"],
    "age": [25, 30, 35, 28],
    "salary": [50000, 65000, 70000, 55000],
    "city": ["Chicago", "New York", "Chicago", "Boston"]
})

# ============================================================
# 2. INSPECT DATA
# ============================================================

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

# ============================================================
# 3. READ / WRITE FILES
# ============================================================

# CSV
df = pd.read_csv("customers.csv")

# Save CSV
df.to_csv("output.csv", index=False)

# JSON
df = pd.read_json("customers.json")
df.to_json("output.json", orient="records")

# Parquet - very important in Data Engineering
df = pd.read_parquet("customers.parquet")
df.to_parquet("output.parquet", index=False)

# ============================================================
# 4. SELECT COLUMNS
# ============================================================

df["name"]

df[["name", "age", "salary"]]

# ============================================================
# 5. LOC / ILOC
# ============================================================

# Label-based
df.loc[0:2, ["name", "salary"]]

# Position-based
df.iloc[0:3, 0:3]

# ============================================================
# 6. FILTERING
# ============================================================

result = df[df["age"] > 30]

result = df[
    (df["age"] > 25) &
    (df["salary"] > 50000)
]

result = df[
    df["city"].isin(["Chicago", "Boston"])
]

# ============================================================
# 7. ADD / MODIFY COLUMNS
# ============================================================

df["bonus"] = df["salary"] * 0.10

df["salary"] = df["salary"] + 5000

# ============================================================
# 8. MISSING VALUES
# ============================================================

print(df.isna().sum())

df["salary"] = df["salary"].fillna(0)

df = df.dropna()

# ============================================================
# 9. DUPLICATES
# ============================================================

print(df.duplicated().sum())

df = df.drop_duplicates()

df = df.drop_duplicates(
    subset=["customer_id"]
)

# ============================================================
# 10. DATA TYPE CONVERSION
# ============================================================

df["age"] = df["age"].astype(int)

df["salary"] = df["salary"].astype(float)

df["created_at"] = pd.to_datetime(
    df["created_at"]
)

# ============================================================
# 11. STRING CLEANING
# ============================================================

df["name"] = df["name"].str.strip()

df["name"] = df["name"].str.lower()

df["email"] = df["email"].str.lower()

df["email"] = df["email"].str.replace(
    " ",
    "",
    regex=False
)

# ============================================================
# 12. SORTING
# ============================================================

df = df.sort_values(
    "salary",
    ascending=False
)

# ============================================================
# 13. GROUPBY / AGGREGATION
# ============================================================

result = df.groupby("city").agg(
    total_salary=("salary", "sum"),
    average_salary=("salary", "mean"),
    employee_count=("customer_id", "count")
)

print(result)

# ============================================================
# 14. MERGE
# ============================================================

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["John", "Mary", "David"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "customer_id": [1, 2, 1],
    "amount": [100, 200, 150]
})

result = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)

print(result)

# ============================================================
# 15. CONCAT
# ============================================================

df1 = pd.DataFrame({
    "id": [1, 2]
})

df2 = pd.DataFrame({
    "id": [3, 4]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

# ============================================================
# 16. DATETIME
# ============================================================

df["created_at"] = pd.to_datetime(
    df["created_at"]
)

df["year"] = df["created_at"].dt.year
df["month"] = df["created_at"].dt.month
df["day"] = df["created_at"].dt.day

# ============================================================
# 17. APPLY / TRANSFORMATION
# ============================================================

df["salary_category"] = df["salary"].apply(
    lambda x: "High" if x >= 70000 else "Low"
)

# ============================================================
# 18. LARGE FILES / CHUNKS
# ============================================================

for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=100000
):
    # Process each chunk
    print(chunk.shape)

# ============================================================
# 19. DATA QUALITY CHECK
# ============================================================

print("Rows:", len(df))

print("Missing:")
print(df.isna().sum())

print("Duplicates:")
print(df.duplicated().sum())

print("Data Types:")
print(df.dtypes)

# ============================================================
# 20. SIMPLE ETL
# ============================================================

# Extract
raw_df = pd.read_csv("customers.csv")

# Transform
raw_df = raw_df.drop_duplicates(
    subset=["customer_id"]
)

raw_df["name"] = (
    raw_df["name"]
    .str.strip()
    .str.lower()
)

raw_df["created_at"] = pd.to_datetime(
    raw_df["created_at"]
)

raw_df["salary"] = (
    raw_df["salary"]
    .fillna(0)
)

# Load
raw_df.to_parquet(
    "clean_customers.parquet",
    index=False
)
```


