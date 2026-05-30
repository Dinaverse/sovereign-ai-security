# 🛡️ Sovereign AI Security: NVIDIA Morpheus & Triton Integration

This repository features advanced, AI-driven security tools designed to leverage **NVIDIA Morpheus**, **Triton Inference Server**, and **DeepStream** for high-performance threat detection and secret scanning.

## 🚀 Key Features

### 🔍 AI Secret Scanning (Morpheus SID)
- **`scan_secrets_ia_pro.py`**: A professional-grade scanner utilizing a BERT tokenizer and NVIDIA Triton Inference Server to detect sensitive information (passwords, API keys, PII) across various file types.
- **`scan_secrets_ia.py`**: A simplified bridge script for testing files against a local Morpheus SID (Sensitive Information Detection) model.

### 🛰️ Security Tool Bridge
- **`security_tool_bridge.py`**: An autonomous orchestration script that monitors data intake directories and routes files to specialized AI analysis containers:
    - **Images:** Analyzed via **DeepStream** for computer vision-based security tasks.
    - **Logs/JSON:** Analyzed via **cyBERT** for advanced network threat detection.

## 🏗️ Architecture
The tools in this repository are designed to operate as part of a distributed, sovereign security lab, where data is processed locally using containerized NVIDIA-optimized models.

---
*Securing the distributed frontier with AI - Developed by Dina.*
