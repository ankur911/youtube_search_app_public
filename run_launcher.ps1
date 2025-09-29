# YouTube Search App Launcher - Fixed Version
Write-Host "YouTube Search App Launcher" -ForegroundColor Green
Write-Host "=============================" -ForegroundColor Green

# Check and activate virtual environment
if (Test-Path ".\youtube_env\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..." -ForegroundColor Green
    & ".\youtube_env\Scripts\Activate.ps1"
} else {
    Write-Host "Virtual environment not found!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Choose which app to run:" -ForegroundColor Yellow
Write-Host "1. Streamlit (Web interface)"
Write-Host "2. Gradio (Alternative interface)"
Write-Host "3. Console (Original script)"
Write-Host "4. Install packages"
Write-Host "5. Environment info"
Write-Host ""

$choice = Read-Host "Enter your choice (1-5)"

if ($choice -eq "1") {
    Write-Host "Starting Streamlit..." -ForegroundColor Green
    Write-Host "Will open at: http://localhost:8501" -ForegroundColor Yellow
    python -m streamlit run src/youtube_frontend.py
}
elseif ($choice -eq "2") {
    Write-Host "Starting Gradio..." -ForegroundColor Green
    Write-Host "Will open automatically in browser" -ForegroundColor Yellow
    python src/youtube_gradio.py
}
elseif ($choice -eq "3") {
    Write-Host "Running console script..." -ForegroundColor Green
    python src/youtube_search.py
}
elseif ($choice -eq "4") {
    Write-Host "Installing/Updating packages..." -ForegroundColor Green
    pip install -r requirements.txt
    Write-Host "Packages updated!" -ForegroundColor Green
    Read-Host "Press Enter to continue"
}
elseif ($choice -eq "5") {
    Write-Host "Environment Information:" -ForegroundColor Green
    Write-Host "Python version:"
    python --version
    Write-Host "Virtual environment path:"
    python -c "import sys; print(sys.executable)"
    Write-Host "Installed packages:"
    pip list | Select-String "streamlit|gradio|google"
    Read-Host "Press Enter to continue"
}
else {
    Write-Host "Invalid choice. Please run the script again." -ForegroundColor Red
    Read-Host "Press Enter to exit"
}