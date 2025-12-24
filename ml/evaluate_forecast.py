import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from pathlib import Path

DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "cpu_forecast.csv"

df = pd.read_csv(CSV_PATH)
df["timestamp"] = pd.to_datetime(df["timestamp"])

actual = df[df["type"] == "actual"].tail(10)
forecast = df[df["type"] == "forecast"].head(len(actual))

# Align lengths defensively
min_len = min(len(actual), len(forecast))
actual = actual.iloc[:min_len]
forecast = forecast.iloc[:min_len]

mae = mean_absolute_error(actual["cpu_usage_percent"],
                          forecast["cpu_usage_percent"])

rmse = np.sqrt(mean_squared_error(actual["cpu_usage_percent"],
                                  forecast["cpu_usage_percent"]))

print("Forecast Evaluation")
print("-------------------")
print(f"MAE  : {mae:.3f}")
print(f"RMSE : {rmse:.3f}")

