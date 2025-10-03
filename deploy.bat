@echo off
echo 🚀 YouTube Search App - Streamlit Deployment Script (Windows)
echo ==============================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️  .env file not found. Creating template...
    echo API_KEY=your_youtube_api_key_here > .env
    echo 📝 Please edit .env file and add your YouTube API key
    echo    You can get one from: https://console.cloud.google.com/
    echo.
)

echo.
echo 🎉 Setup complete!
echo.
echo To start the app:
echo 1. Make sure you've set your API_KEY in the .env file
echo 2. Run: streamlit run streamlit_app.py
echo.
echo The app will be available at:
echo   🏠 Local: http://localhost:8501
echo   🌐 Network: Use --server.address=0.0.0.0 for network access
echo.
echo For network access (other devices on same network):
echo   streamlit run streamlit_app.py --server.address=0.0.0.0
echo.
echo Happy searching! 🎥
echo.
pause