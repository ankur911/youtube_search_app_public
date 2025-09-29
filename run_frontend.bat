@echo off
echo Starting YouTube Search Frontend Applications...
echo.

echo Choose which frontend to run:
echo 1. Streamlit (Web-based, modern UI)
echo 2. Gradio (Simple, clean interface)
echo 3. Original console script
echo.

set /p choice="Enter your choice (1, 2, or 3): "

if "%choice%"=="1" (
    echo Starting Streamlit...
    python -m streamlit run youtube_frontend.py
) else if "%choice%"=="2" (
    echo Starting Gradio...
    python youtube_gradio.py
) else if "%choice%"=="3" (
    echo Running original script...
    python youtube_search.py
) else (
    echo Invalid choice. Please run the script again.
    pause
)