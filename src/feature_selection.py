import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

# =========================
# LOAD DATASET
# =========================

file_path = "../data/processed/dataset_cleaned.csv"

df = pd.read_csv(file_path)

print("Dataset Loaded")

# =========================
# SPLIT X AND y
# =========================

X = df.drop("Label", axis=1)

y = df["Label"]

print("X Shape:", X.shape)

# =========================
# TRAIN RANDOM FOREST
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

print("\nTraining Random Forest...")

model.fit(X, y)

print("Training Completed")

# =========================
# FEATURE IMPORTANCE
# =========================

importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

# =========================
# SORT FEATURES
# =========================

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)

# =========================
# TOP 20 FEATURES
# =========================

top_20 = feature_importance.head(20)

print("\nTop 20 Features:\n")

print(top_20)

# =========================
# SAVE TOP FEATURES
# =========================

top_20.to_csv(
    "../reports/top_20_features.csv",
    index=False
)

print("\nTop 20 features saved!")

# =========================
# VISUALIZATION
# =========================

plt.figure(figsize=(12, 8))

plt.barh(
    top_20["Feature"],
    top_20["Importance"]
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.title("Top 20 Important Features")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig("../reports/top_20_features.png")

plt.show()