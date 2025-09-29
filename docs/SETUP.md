# 🚀 Setup Guide

## Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- Internet connection
- Google Cloud Console access

## Step-by-Step Setup

### 1. Environment Setup

#### Clone Repository
```bash
git clone <your-repo-url>
cd youtube-search-app
```

#### Create Virtual Environment
```bash
# Windows
python -m venv youtube_env
.\youtube_env\Scripts\Activate.ps1

# Linux/Mac
python -m venv youtube_env
source youtube_env/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. YouTube API Setup

#### Get API Key
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing one
3. Enable "YouTube Data API v3":
   - Go to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click "Enable"
4. Create API Key:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "API Key"
   - Copy the generated key

#### Configure Environment
```bash
# Copy template
cp config/.env.template .env

# Edit .env file
# Replace YOUR_API_KEY_HERE with your actual API key
```

### 3. Verification

#### Test Installation
```bash
# Activate virtual environment
.\youtube_env\Scripts\Activate.ps1  # Windows
source youtube_env/bin/activate     # Linux/Mac

# Test console version
python src/youtube_search.py

# Test Streamlit
python -m streamlit run src/youtube_frontend.py

# Test Gradio
python src/youtube_gradio.py
```

## Troubleshooting

### Python Version Issues
```bash
# Check Python version
python --version

# If too old, install newer Python from python.org
```

### Permission Issues (Windows)
```powershell
# If script execution is blocked
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### API Quota Exceeded
- YouTube Data API has daily quotas
- Free tier: 10,000 units per day
- Each search costs ~100 units
- Monitor usage in Google Cloud Console

### Network Issues
```bash
# Test internet connectivity
ping google.com

# Test API connectivity
curl "https://www.googleapis.com/youtube/v3/search?part=snippet&q=test&key=YOUR_API_KEY"
```

## Quick Launcher

Use the provided launcher script for easy access:

```bash
# Windows PowerShell
.\run_launcher.ps1

# This script will:
# 1. Activate virtual environment
# 2. Show menu of options
# 3. Launch your chosen interface
```