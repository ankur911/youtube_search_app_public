# YouTube Search App - Streamlit Deployment

## Overview
This is a YouTube search application built with Streamlit that allows users to search and watch YouTube videos directly in the web interface.

## Features
- 🔍 Search YouTube videos with custom parameters
- ▶️ Watch videos directly in the app
- 🎛️ Advanced search options (duration, region, quality, etc.)
- 📱 Responsive design that works on different devices
- 🌐 Cross-platform deployment support

## Quick Start (Local)

### Prerequisites
- Python 3.8 or higher
- YouTube Data API v3 key

### Installation
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```
   API_KEY=your_youtube_api_key_here
   ```

4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)
1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository
5. Set the main file path to: `streamlit_app.py`
6. Add your API key in the secrets section:
   ```toml
   API_KEY = "your_youtube_api_key_here"
   ```
7. Click "Deploy"

### Option 2: Railway
1. Connect your GitHub repository to Railway
2. Set the start command to: `streamlit run streamlit_app.py --server.port $PORT`
3. Add environment variable: `API_KEY=your_youtube_api_key_here`

### Option 3: Heroku
1. Create a `Procfile` with: `web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
2. Add environment variable: `API_KEY=your_youtube_api_key_here`
3. Deploy through Heroku CLI or GitHub integration

### Option 4: Local Network Access
To allow others on your local network to access the app:
```bash
streamlit run streamlit_app.py --server.address=0.0.0.0
```
Then share your local IP address (e.g., `http://192.168.1.100:8501`)

## Environment Variables
- `API_KEY`: Your YouTube Data API v3 key (required)

## Getting a YouTube API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the YouTube Data API v3
4. Create credentials (API key)
5. Restrict the key to YouTube Data API v3 for security

## File Structure
```
youtube_search_app/
├── streamlit_app.py          # Main entry point for deployment
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── src/
│   ├── youtube_frontend.py  # Main application code
│   └── youtube_search.py    # Search functionality
└── README.md               # This file
```

## Troubleshooting

### API Key Issues
- Ensure your API key is valid and has YouTube Data API v3 enabled
- Check that you haven't exceeded your daily quota
- Verify the API key is correctly set in environment variables

### Deployment Issues
- Make sure all dependencies are listed in `requirements.txt`
- Check that the Python version is compatible (3.8+)
- Verify environment variables are properly set

### Video Playback Issues
- Some videos may not be embeddable due to creator restrictions
- Try different search terms if videos don't load
- Check your internet connection

## Support
If you encounter any issues, please check the troubleshooting section above or create an issue in the repository.

## License
This project is open source and available under the MIT License.