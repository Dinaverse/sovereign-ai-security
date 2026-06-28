# 🛡️ Sovereign AI Security

> *AI-driven security tooling built on NVIDIA Morpheus, Triton Inference Server, and custom Python pipelines designed for high-performance, local threat detection without cloud exposure.*

---

## 🎯 Overview

This repository implements an AI-augmented security layer for the sovereign lab. It leverages GPU-accelerated inference to perform real-time secret scanning, anomaly detection, and threat analysis entirely on local hardware no external API calls, no data leakage.

---

## 🚀 Key Components

### 🔍 AI Secret Scanner (`scan_secrets_ia_pro.py`)
Professional-grade secret and PII detection using a BERT tokenizer backed by NVIDIA Triton Inference Server. Scans codebases, configuration files, and logs for exposed credentials, API keys, and sensitive data patterns.

### ⚡ Lightweight Scanner (`scan_secrets_ia.py`)
Simplified bridge script for rapid scanning in resource-constrained environments same detection logic, minimal dependencies.

---

## 🧰 Technology Stack

```text
🤖 AI Framework    ::  NVIDIA Morpheus (cybersecurity AI pipeline)
🖥️ Inference       ::  NVIDIA Triton Inference Server
🧠 Model           ::  BERT tokenizer (local, no cloud)
🐍 Language        ::  Python 3.x
🎮 Acceleration    ::  CUDA / NVIDIA GPU
🐳 Deployment      ::  Docker containerized
```

---

## 🏗️ Architecture

```
[Log / File Input]
       │
[Morpheus Pipeline]
       │
[Triton Inference Server] ←── BERT Tokenizer (local model)
       │
[Threat Classification]
       │
[Alert / Report Output]
```

---

## 🔗 Lab Integration

This tooling operates within the broader sovereign security stack:

| Component | Repository |
|-----------|------------|
| Security automation scripts | [`cybersecurity-lab-automation`](https://github.com/Dinaverse/cybersecurity-lab-automation) |
| Python security scanners | [`python-security-analytics`](https://github.com/Dinaverse/python-security-analytics) |
| Core infrastructure | [`sovereign-ai-infrastructure`](https://github.com/Dinaverse/sovereign-ai-infrastructure) |

---

*No cloud. No telemetry. Full control.*
