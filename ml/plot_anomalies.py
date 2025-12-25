import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ml/data/cpu_with_anomalies.csv") #This path has to be edited as per needed
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(12, 6))

# Normal points
normal = df[df["anomaly"] == 0]
plt.plot(
    normal["timestamp"],
    normal["cpu_usage_percent"],
    marker="o",
    linestyle="-",
    label="Normal"
)

# Anomalies
anomalies = df[df["anomaly"] == 1]
plt.scatter(
    anomalies["timestamp"],
    anomalies["cpu_usage_percent"],
    label="Anomaly"
)

plt.title("CPU Usage Anomaly Detection (Isolation Forest)")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("ml/data/cpu_anomalies.png") #This path has to be edited as per needed
print("[OK] Plot saved to ml/data/cpu_anomalies.png")


