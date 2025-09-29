Write-Host "Starting YouTube Search Frontend Applications..." -ForegroundColor Green
Write-Host ""

Write-Host "Choose which frontend to run:" -ForegroundColor Yellow
Write-Host "1. Streamlit (Web-based, modern UI)"
Write-Host "2. Gradio (Simple, clean interface)"
Write-Host "3. Original console script"
Write-Host ""

$choice = Read-Host "Enter your choice (1, 2, or 3)"

switch ($choice) {
    "1" {
        Write-Host "Starting Streamlit..." -ForegroundColor Green
        python -m streamlit run youtube_frontend.py
    }
    "2" {
        Write-Host "Starting Gradio..." -ForegroundColor Green
        python youtube_gradio.py
    }
    "3" {
        Write-Host "Running original script..." -ForegroundColor Green
        python youtube_search.py
    }
    default {
        Write-Host "Invalid choice. Please run the script again." -ForegroundColor Red
        Read-Host "Press Enter to exit"
    }
}