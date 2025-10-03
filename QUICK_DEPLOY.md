# 🚀 Quick Deployment Guide

## Streamlit Cloud (Easiest Option)

### Step 1: Prepare Repository
1. Push your code to GitHub (your repository is already ready!)
2. Make sure these files are in your repo:
   - `streamlit_app.py` ✅
   - `requirements.txt` ✅
   - `.streamlit/config.toml` ✅

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `ankur911/youtube_search_app`
5. Set main file path: `streamlit_app.py`
6. Click "Advanced settings"
7. Add your YouTube API key in secrets:
   ```toml
   API_KEY = "your_actual_youtube_api_key_here"
   ```
8. Click "Deploy"

### Step 3: Share Your App
Once deployed, you'll get a URL like:
`https://your-app-name.streamlit.app`

## Local Testing (Before Deployment)

### Windows:
```powershell
# Run the deployment script
.\deploy.ps1

# Or manually:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Edit .env file with your API key
streamlit run streamlit_app.py
```

### Linux/macOS:
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Edit .env file with your API key
streamlit run streamlit_app.py
```

## Other Deployment Options

### Railway
1. Connect GitHub repo to Railway
2. Set start command: `streamlit run streamlit_app.py --server.port $PORT`
3. Add environment variable: `API_KEY=your_key`

### Heroku
1. Use the included `Procfile`
2. Set environment variable: `API_KEY=your_key`
3. Deploy via Git or GitHub integration

### Render
1. Connect GitHub repo
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0`
4. Add environment variable: `API_KEY=your_key`

## Getting YouTube API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project or select existing
3. Enable "YouTube Data API v3"
4. Create credentials → API Key
5. Restrict key to YouTube Data API v3

## Files Created for Deployment
- `src/youtube_frontend_deploy.py` - Deployment-optimized frontend
- `streamlit_app.py` - Entry point for deployment
- `.streamlit/config.toml` - Streamlit configuration
- `Procfile` - For Heroku deployment
- `deploy.ps1` / `deploy.bat` - Windows deployment scripts
- `DEPLOYMENT_README.md` - Detailed deployment guide

## Testing Different Locations/OS
Once deployed on Streamlit Cloud or other platforms, anyone can access your app from:
- ✅ Windows, macOS, Linux
- ✅ Mobile devices (iOS, Android)
- ✅ Different browsers
- ✅ Any internet connection worldwide

Your app will be accessible 24/7 without needing your computer running!