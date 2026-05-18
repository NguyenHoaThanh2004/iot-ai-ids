import joblib

# =========================
# LOAD MODEL
# =========================

model_path = "../models/rf_model.pkl"

model = joblib.load(model_path)

print("Model Loaded Successfully!")

print(model)