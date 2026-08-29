@echo off

echo Starting llama.cpp...

"..\llama-cpp\llama-server.exe" ^
-m "..\models\glm\GLM-4.7-Flash-Q4_K.gguf" ^
--gpu-layers 20 --port 8080 --temp 1.0 --top-p 0.95 --min-p 0.01

:: gpu layers tuned based on hardware requirements
:: model hyperparameters recommended by https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF
pause