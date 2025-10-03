# YouTube Search App - Streamlit Deployment Script (PowerShell)
Write-Host "🚀 YouTube Search App - Streamlit Deployment Script" -ForegroundColor Cyan
Write-Host "======================================================" -ForegroundColor Cyan

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Python detected: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python not found"
    }
} catch {
    Write-Host "❌ Python is not installed or not in PATH. Please install Python 3.8 or higher." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "🔄 Activating virtual environment..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "⚠️  .env file not found. Creating template..." -ForegroundColor Yellow
    "API_KEY=your_youtube_api_key_here" | Out-File -FilePath ".env" -Encoding UTF8
    Write-Host "📝 Please edit .env file and add your YouTube API key" -ForegroundColor Magenta
    Write-Host "   You can get one from: https://console.cloud.google.com/" -ForegroundColor Magenta
    Write-Host ""
}

# Get local IP address for network access
try {
    $localIP = (Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias "Wi-Fi*","Ethernet*" | Where-Object {$_.IPAddress -notlike "169.*"} | Select-Object -First 1).IPAddress
    if (-not $localIP) {
        $localIP = "localhost"
    }
} catch {
    $localIP = "localhost"
}

Write-Host ""
Write-Host "🎉 Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "To start the app:" -ForegroundColor Cyan
Write-Host "1. Make sure you've set your API_KEY in the .env file" -ForegroundColor White
Write-Host "2. Run: streamlit run streamlit_app.py" -ForegroundColor White
Write-Host ""
Write-Host "The app will be available at:" -ForegroundColor Cyan
Write-Host "  🏠 Local: http://localhost:8501" -ForegroundColor White
if ($localIP -ne "localhost") {
    Write-Host "  🌐 Network: http://$localIP`:8501" -ForegroundColor White
}
Write-Host ""
Write-Host "For network access (other devices on same network):" -ForegroundColor Cyan
Write-Host "  streamlit run streamlit_app.py --server.address=0.0.0.0" -ForegroundColor White
Write-Host ""
Write-Host "For cloud deployment options, see DEPLOYMENT_README.md" -ForegroundColor Magenta
Write-Host ""
Write-Host "Happy searching! 🎥" -ForegroundColor Green

Read-Host "Press Enter to continue"