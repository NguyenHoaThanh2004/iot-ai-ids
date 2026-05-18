import pandas as pd
import numpy as np

# =========================
# LOAD DATASET
# =========================

file_path = "../data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:")
print(df.shape)

# =========================
# CLEAN COLUMN NAMES
# =========================

df.columns = df.columns.str.strip()

print("\nColumns cleaned")

# =========================
# REMOVE USELESS COLUMNS
# =========================

drop_columns = [
    "Flow ID",
    "Source IP",
    "Destination IP",
    "Timestamp"
]

df.drop(columns=drop_columns, inplace=True)

print("\nDropped useless columns")

# =========================
# HANDLE INFINITY
# =========================

df.replace([np.inf, -np.inf], np.nan, inplace=True)

# =========================
# REMOVE NaN
# =========================

df.dropna(inplace=True)

print("\nRemoved NaN and Infinity")

# =========================
# ENCODE LABEL
# =========================

df["Label"] = df["Label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

print("\nEncoded labels")

# =========================
# CHECK LABEL DISTRIBUTION
# =========================

print("\nLabel Distribution:")

print(df["Label"].value_counts())

# =========================
# SAVE CLEAN DATASET
# =========================

output_path = "../data/processed/dataset_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved!")

print("\nFinal Shape:")
print(df.shape)