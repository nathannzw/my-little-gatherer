@echo off
title My Little Gatherer - Launcher

rem Resolve the repo root from this script's own location (no hardcoded paths).
rem %~dp0 is the directory containing this .bat, with a trailing backslash.
pushd "%~dp0.."
set "ROOT=%CD%"
popd

echo Repo root: %ROOT%

echo Starting LLM server...
start "LLM Server" /D "%ROOT%" cmd /k "llama serve -m .\models\qwen\Qwen3.5-4B-UD-Q8_K_XL.gguf -ngl 99 --port 8080 --temp 1.0 --top-p 0.95 --min-p 0.01 --flash-attn on"

echo Starting backend...
start "Backend" /D "%ROOT%\server" cmd /k "uv run uvicorn gatherer.api.main:app --reload --port 8000"

echo Starting frontend...
start "Frontend" /D "%ROOT%\client" cmd /k "npm run dev"

echo.
echo All services launched.
pause