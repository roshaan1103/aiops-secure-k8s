import pandas as pd

ANOMALY_THRESHOLD = -1          # Isolation Forest output
FORECAST_CPU_THRESHOLD = 75.0   # %

anomaly_file = "ml/data/cpu_with_anomalies.csv"
forecast_file = "ml/data/cpu_forecast.csv"

decisions = []

# --- Load anomaly results ---
anomalies = pd.read_csv(anomaly_file)
latest_anomaly = anomalies.iloc[-1]

if latest_anomaly["anomaly"] == ANOMALY_THRESHOLD:
    decisions.append("CPU_ANOMALY_DETECTED")

# --- Load forecast results ---
forecast = pd.read_csv(forecast_file)
future_forecast = forecast[forecast["type"] == "forecast"]

if future_forecast["cpu_usage_percent"].max() > FORECAST_CPU_THRESHOLD:
    decisions.append("CPU_OVERLOAD_PREDICTED")

# --- Final decision ---
if not decisions:
    decision = "SYSTEM_NORMAL"
else:
    decision = ",".join(decisions)

print(f"[DECISION] {decision}")

# Save decision
with open("data/decision.txt", "w") as f:
    f.write(decision)

