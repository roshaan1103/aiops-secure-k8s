import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ml/data/cpu_usage_percent.csv") #This path has to be edited later as per needed

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Feature matrix
X = df[["cpu_usage_percent"]]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,   # 5% anomalies (reasonable default)
    random_state=42
)

df["anomaly"] = model.fit_predict(X)

# -1 = anomaly, 1 = normal
df["anomaly"] = df["anomaly"].map({1: 0, -1: 1})

# Save results
df.to_csv("ml/data/cpu_with_anomalies.csv", index=False) #This path has to be edited as per needed

print(f"[OK] Detected {df['anomaly'].sum()} anomalies")

