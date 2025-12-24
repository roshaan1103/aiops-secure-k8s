import subprocess

DECISION_FILE = "data/decision.txt"
DRY_RUN = False   # IMPORTANT

with open(DECISION_FILE) as f:
    decision = f.read().strip()

print(f"[ACTUATOR] Decision received: {decision}")

def run(cmd):
    print("[DRY-RUN]" if DRY_RUN else "[EXEC]", cmd)
    if not DRY_RUN:
        subprocess.run(cmd, shell=True, check=True)

if decision == "CPU_ANOMALY_DETECTED":
    run("kubectl rollout restart deployment demo-app -n demo")

elif decision == "CPU_OVERLOAD_PREDICTED":
    run("kubectl scale deployment demo-app -n demo --replicas=3")

elif decision == "SYSTEM_NORMAL":
    print("[ACTUATOR] No action required.")

else:
    print("[ACTUATOR] Unknown decision.")

