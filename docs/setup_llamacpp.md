# Local LLM Setup Guide

This guide walks you through installing **llama.cpp** and hosting **GLM-4.7-Flash** locally using GPU offloading on Windows.

## Prerequisites

- **OS:** Windows 10 / 11
- **GPU:** NVIDIA GPU with updated CUDA drivers (e.g., RTX 4070 Super)
- **RAM:** 32 GB system RAM recommended for hybrid offloading

---

## Step 1: Install llama.cpp

Open **PowerShell** or **Command Prompt** and run:

```powershell
winget install llama.cpp
```

---

## Step 2: Download & Run GLM-4.7-Flash

Execute the following command to download the 4-bit quantized GGUF model and start the OpenAI-compatible REST server:

```powershell
llama-server -hf ggml-org/GLM-4.7-Flash-GGUF:Q4_K --repeat-penalty 1.0 -ngl 32
```

---

## Command Parameter Breakdown

| Parameter | Function |
|-----------|----------|
| `-hf ggml-org/GLM-4.7-Flash-GGUF:Q4_K` | Automatically downloads and loads the Q4_K GGUF model from Hugging Face. |
| `--repeat-penalty 1.0` | Prevents token repetition or output looping (recommended for GLM-4.7). |
| `-ngl 32` | Offloads 32 transformer layers to the GPU (VRAM), leaving the remaining layers in system RAM. |

---

## Server Connection Information

Once the server is running, connect your RAG application to the local endpoint.

| Setting | Value |
|---------|-------|
| **Base URL** | `http://127.0.0.1:8080/v1` |
| **API Key** | `not-needed` (or any placeholder string) |
| **Health Endpoint** | `http://127.0.0.1:8080/health` |