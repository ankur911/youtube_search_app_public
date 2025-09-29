# YouTube Search Virtual Environment Launcher (Updated for new structure)
# This script activates the virtual environment and runs the frontend

Write-Host "🚀 YouTube Search App Launcher" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path ".\youtube_env\Scripts\Activate.ps1")) {
    Write-Host "❌ Virtual environment not found!" -ForegroundColor Red
    Write-Host "Please run the setup first or check if you're in the right directory." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Activating virtual environment..." -ForegroundColor Green

# Activate virtual environment
& ".\youtube_env\Scripts\Activate.ps1"

Write-Host ""
Write-Host "🎯 Choose which app to run:" -ForegroundColor Yellow
Write-Host "1. 🌐 Streamlit (Modern web interface)" -ForegroundColor Cyan
Write-Host "2. 🎛️ Gradio (Simple interface)" -ForegroundColor Cyan
Write-Host "3. 💻 Console (Original script)" -ForegroundColor Cyan
Write-Host "4. 🔧 Install/Update packages" -ForegroundColor Magenta
Write-Host "5. 📋 Show environment info" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-5)"

switch ($choice) {
    "1" {
        Write-Host "🌐 Starting Streamlit..." -ForegroundColor Green
        Write-Host "📍 Will open at: http://localhost:8501" -ForegroundColor Yellow
        python -m streamlit run src/youtube_frontend.py
    }
    "2" {
        Write-Host "🎛️ Starting Gradio..." -ForegroundColor Green
        Write-Host "📍 Will open automatically in browser" -ForegroundColor Yellow
        python src/youtube_gradio.py
    }
    "3" {
        Write-Host "💻 Running console script..." -ForegroundColor Green
        python src/youtube_search.py
    }
    "4" {
        Write-Host "🔧 Installing/Updating packages..." -ForegroundColor Green
        pip install -r requirements.txt
        Write-Host "✅ Packages updated!" -ForegroundColor Green
        Read-Host "Press Enter to continue"
    }
    "5" {
        Write-Host "📋 Environment Information:" -ForegroundColor Green
        Write-Host "Python version:" -ForegroundColor Yellow
        python --version
        Write-Host "Virtual environment path:" -ForegroundColor Yellow
        python -c "import sys; print(sys.executable)"
        Write-Host "Installed packages:" -ForegroundColor Yellow
        pip list | Select-String "streamlit|gradio|google"
        Read-Host "Press Enter to continue"
    }
    default {
        Write-Host "❌ Invalid choice. Please run the script again." -ForegroundColor Red
        Read-Host "Press Enter to exit"
    }
}