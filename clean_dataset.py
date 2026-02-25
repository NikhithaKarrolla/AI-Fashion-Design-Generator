import pandas as pd

df = pd.read_csv("dataset/Fashion Dataset.csv")

# Select only required columns from YOUR dataset
df = df[['p_id','name','price','colour','brand']]

# Remove missing values
df = df.dropna()

# Convert p_id to integer (remove .0)
df['p_id'] = df['p_id'].astype(int)

df.to_csv("dataset/cleaned_fashion_data.csv", index=False)

print("Dataset Cleaned Successfully")