import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# =========================
# LOAD DATASET
# =========================

csv_files = glob.glob("../data/raw/*.csv")

df = pd.read_csv(csv_files[0])

# =========================
# CLEAN DATA
# =========================

df.columns = df.columns.str.strip()

df.replace([np.inf, -np.inf], np.nan, inplace=True)

df.dropna(inplace=True)

# =========================
# LABEL ENCODING
# =========================

df["Label"] = df["Label"].apply(
    lambda x: 0 if x == "BENIGN" else 1
)

# =========================
# FEATURES
# =========================

drop_columns = [
    "Flow ID",
    "Source IP",
    "Destination IP",
    "Timestamp",
    "Label"
]

X = df.drop(columns=drop_columns)

X = X.select_dtypes(include=["number"])

y = df["Label"]

# =========================
# SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# TRAIN MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# =========================
# FEATURE IMPORTANCE
# =========================

importance = model.feature_importances_

feature_names = X.columns

feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)

# TOP 10
top_features = feature_df.head(10)

# =========================
# PLOT
# =========================

plt.figure(figsize=(10, 6))

plt.barh(
    top_features["Feature"],
    top_features["Importance"]
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.title("Top 10 Important Features - AI IDS")

plt.gca().invert_yaxis()

plt.tight_layout()

# =========================
# SAVE IMAGE
# =========================

plt.savefig("../logs/feature_importance.png")

print("\nFeature Importance Saved!")