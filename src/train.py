import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# =========================
# LOAD DATASET
# =========================

file_path = "../data/processed/dataset_cleaned.csv"

df = pd.read_csv(file_path)

print("Dataset Loaded")

# =========================
# SPLIT FEATURES & LABEL
# =========================

X = df.drop("Label", axis=1)

y = df["Label"]

print("X Shape:", X.shape)

print("y Shape:", y.shape)

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain/Test Split Completed")

print("X_train:", X_train.shape)

print("X_test:", X_test.shape)

# =========================
# BUILD MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

print("\nTraining Model...")

# =========================
# TRAIN MODEL
# =========================

model.fit(X_train, y_train)

print("Training Completed")

# =========================
# PREDICTION
# =========================

y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")

print(accuracy)

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, y_pred))

# =========================
# SAVE MODEL
# =========================

model_path = "../models/rf_model.pkl"

joblib.dump(model, model_path)

print("\nModel Saved!")

print("\nPath:")

print(model_path)