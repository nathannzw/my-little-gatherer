@echo off

echo Starting llama.cpp server...

:: Start the local HTTP server with the Qwen model from Hugging Face
:: This downloads the GGUF model automatically from the Hugging Face hub
:: and exposes the OpenAI-compatible API on http://127.0.0.1:8080
llama serve -m ../models/qwen/Qwen3.5-4B-UD-Q8_K_XL.gguf -ngl 99 --port 8080 --temp 1.0 --top-p 0.95 --min-p 0.01 --flash-attn on

:: Offload up to 99 transformer layers to the GPU; reduce if VRAM is limited
:: Sampling temperature: lower values make output more deterministic
:: Top-p nucleus sampling: keeps only the most likely token mass
:: Min-p sampling: filters very low-probability tokens to avoid garbage output
:: Enable flash attention when supported by the build and GPU
:: gpu layers tuned based on hardware requirements
:: model hyperparameters recommended by https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF
:: for directly download llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF -ngl 99 --port 8080 --temp 1.0 --top-p 0.95 --min-p 0.01 --flash-attn on
pause