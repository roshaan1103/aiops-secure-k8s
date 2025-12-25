Project: Secure AIOps Pipeline for Kubernetes

Problem:

Kubernetes failures are often detected late, diagnosed manually, and lack predictive insight — especially under resource constraints.

Solution:

A secure, automated AIOps pipeline that:

-> collects live cluster metrics

-> detects anomalies

-> predicts trends

-> enforces least-privilege security

-> produces machine-readable operational decisions\


Architecture:

-> Kubernetes (single-node VM)

-> Prometheus + Node Exporter

-> Python (metrics ingestion, anomaly detection, prediction)

-> Jenkins CI pipeline

-> NetworkPolicies + RBAC for security enforcement


Key Capabilities:

-> Real-time metrics ingestion

-> Statistical anomaly detection

-> Predictive modeling

-> CI-driven automation

-> Security-aware failure handling


Security Controls:

-> NetworkPolicy enforcing Prometheus-only scraping

-> Dedicated ServiceAccount with scoped RBAC

-> Detection of DNS and metrics isolation failures

-> Security failures surfaced as AI decisions


Failure Scenarios Tested:

-> DiskPressure pod eviction

-> DNS outage (CoreDNS CrashLoop)

-> Metrics pipeline disruption

-> RBAC misconfiguration

-> CI artifact contract violations


Outcome:

An end-to-end, security-aware AIOps pipeline capable of detecting, predicting, and explaining Kubernetes infrastructure failures.
