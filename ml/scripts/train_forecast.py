import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from pathlib import Path

# Paths
DATA_DIR = Path("ml/data")
CSV_PATH = DATA_DIR / "cpu_usage_percent.csv"
OUT_CSV = DATA_DIR / "cpu_forecast.csv"
OUT_PNG = DATA_DIR / "cpu_forecast.png"

# Load data
df = pd.read_csv(CSV_PATH)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Index as time
df = df.sort_values("timestamp").reset_index(drop=True)

# Create time index for regression
df["t"] = np.arange(len(df))

X = df[["t"]]
y = df["cpu_usage_percent"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Forecast horizon
FORECAST_STEPS = 10
future_t = np.arange(len(df), len(df) + FORECAST_STEPS).reshape(-1, 1)
forecast_values = model.predict(future_t)

# Build forecast dataframe
last_time = df["timestamp"].iloc[-1]
freq = df["timestamp"].diff().median()

future_times = [last_time + (i + 1) * freq for i in range(FORECAST_STEPS)]

forecast_df = pd.DataFrame({
    "timestamp": future_times,
    "cpu_usage_percent": forecast_values,
    "type": "forecast"
})

history_df = df[["timestamp", "cpu_usage_percent"]].copy()
history_df["type"] = "actual"

final_df = pd.concat([history_df, forecast_df], ignore_index=True)
final_df.to_csv(OUT_CSV, index=False)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(history_df["timestamp"], history_df["cpu_usage_percent"], label="Actual")
plt.plot(forecast_df["timestamp"], forecast_df["cpu_usage_percent"], label="Forecast")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Forecast (Linear Regression Baseline)")
plt.legend()
plt.tight_layout()
plt.savefig(OUT_PNG)
plt.show()

print(f"[OK] Forecast saved to {OUT_CSV}")
print(f"[OK] Plot saved to {OUT_PNG}")

# Risk threshold
CPU_THRESHOLD = 80  # percent

if (forecast_df["cpu_usage_percent"] > CPU_THRESHOLD).any():
    print("[ALERT] Forecast predicts CPU threshold breach")
else:
    print("[OK] No CPU saturation predicted in forecast window")

