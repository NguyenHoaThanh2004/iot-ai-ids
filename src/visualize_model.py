import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report

# =========================
# LOAD DATASET
# =========================

import glob

csv_files = glob.glob("../data/raw/*.csv")

print(csv_files)

df = pd.read_csv(csv_files[0])

# =========================
# CLEAN COLUMN NAMES
# =========================

df.columns = df.columns.str.strip()

# =========================
# REMOVE NaN
# =========================

import numpy as np

df = df.dropna()

# Replace infinity values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove NaN again
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

# Keep numeric only
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
# PREDICT
# =========================

y_pred = model.predict(X_test)

# =========================
# REPORT
# =========================

print(classification_report(y_test, y_pred))

# =========================
# CONFUSION MATRIX
# =========================

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["BENIGN", "ATTACK"]
)

disp.plot()

plt.title("Confusion Matrix - AI IDS")

# =========================
# SAVE IMAGE
# =========================

plt.savefig("../logs/confusion_matrix.png")

print("\nConfusion Matrix Saved!")