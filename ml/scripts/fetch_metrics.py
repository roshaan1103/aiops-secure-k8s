import requests
import time
import csv
import os
from datetime import datetime

PROM_HOST = "localhost"
PROM_PORT = 9090

PROM_URL = f"http://{PROM_HOST}:{PROM_PORT}/api/v1/query_range"

QUERY = '100 * (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[1m])))'

END = int(time.time())
START = END - 10 * 60   # last 10 minutes
STEP = 15              # 15s resolution

PARAMS = {
    "query": QUERY,
    "start": START,
    "end": END,
    "step": STEP
}

response = requests.get(PROM_URL, params=PARAMS, timeout=10)
response.raise_for_status()

data = response.json()

if data["status"] != "success":
    raise Exception("Prometheus query failed")

result = data["data"]["result"]

if not result:
    raise Exception("No metrics returned — check Prometheus targets")

values = result[0]["values"]

# --- NEW PART ---
DATA_DIR = "ml/data"
os.makedirs(DATA_DIR, exist_ok=True)

output_file = os.path.join(DATA_DIR, "cpu_usage_percent.csv")
# ----------------

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "cpu_usage_percent"])

    for ts, value in values:
        ts_readable = datetime.fromtimestamp(int(ts)).strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([ts_readable, float(value)])

print(f"[OK] Saved {len(values)} rows to {output_file}")

