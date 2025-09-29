# 🚀 How to Run YouTube Search App from Virtual Environment
| Command | Description |
|---------|-------------|
| `.\run_launcher.ps1` | Interactive launcher (PowerShell) |
| `run_venv.bat` | Interactive launcher (Command Prompt) |
| `python -m streamlit run src/youtube_frontend.py` | Run Streamlit app |
| `python src/youtube_gradio.py` | Run Gradio app |
| `python src/youtube_search.py` | Run console version |Quick Start (Recommended)

### Option 1: Use the Launcher Scripts
```powershell
# PowerShell (Recommended)
.\run_launcher.ps1

# OR Command Prompt
run_venv.bat
```

### Option 2: Manual Steps
```powershell
# 1. Activate virtual environment
.\youtube_env\Scripts\Activate.ps1

# 2. Run your chosen app
python -m streamlit run youtube_frontend.py    # Streamlit
python youtube_gradio.py                       # Gradio  
python youtube_search.py                       # Console
```

## 🔍 How to Know You're in Virtual Environment

You should see `(youtube_env)` at the beginning of your terminal prompt:
```
(youtube_env) PS D:\Projects\Dream\Youtube>
```

## 🆘 Troubleshooting

### If virtual environment activation fails:
```powershell
# Check if virtual environment exists
ls youtube_env\Scripts\

# If missing, recreate it:
python -m venv youtube_env
.\youtube_env\Scripts\Activate.ps1
pip install -r requirements.txt
```

### If packages are missing:
```powershell
# After activating virtual environment:
pip install -r requirements.txt
```

### Check your current environment:
```powershell
# Show Python path (should point to youtube_env)
python -c "import sys; print(sys.executable)"

# Show installed packages
pip list
```

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `.\run_venv.ps1` | Interactive launcher (PowerShell) |
| `run_venv.bat` | Interactive launcher (Command Prompt) |
| `python -m streamlit run youtube_frontend.py` | Run Streamlit app |
| `python youtube_gradio.py` | Run Gradio app |
| `python youtube_search.py` | Run console version |

## 🌐 Access URLs

- **Streamlit**: http://localhost:8501
- **Gradio**: Opens automatically (usually http://localhost:7860)

## 💡 Tips

1. **Always activate the virtual environment first** before running any Python commands
2. **Use the launcher scripts** for convenience - they handle everything automatically
3. **Check for the `(youtube_env)` prefix** to confirm you're in the right environment
4. **Use Ctrl+C** to stop the web servers when done