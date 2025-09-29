# 🎥 YouTube Search App

A powerful YouTube search application with multiple interfaces built using the YouTube Data API v3. Features both modern web interfaces (Streamlit and Gradio) and a console version for searching and retrieving YouTube videos.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.39.0-red.svg)
![Gradio](https://img.shields.io/badge/gradio-5.6.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🔍 **Advanced YouTube Search** with customizable filters
- 🌐 **Streamlit Web Interface** - Modern, responsive UI with thumbnails
- 🎛️ **Gradio Interface** - Simple, clean alternative interface
- 💻 **Console Version** - Command-line interface for automation
- ⚙️ **Advanced Filtering Options**:
  - Video duration (short/medium/long)
  - Region-specific results
  - Safe search levels
  - Sort by relevance, date, rating, views
  - Video quality filters
  - Custom date ranges
- 🔒 **Secure API Key Management**
- 🐍 **Virtual Environment Support**
- 📋 **Easy Setup Scripts**

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ankur911/Youtube.git
cd Youtube
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv youtube_env

# Activate (Windows)
.\youtube_env\Scripts\Activate.ps1

# Activate (Linux/Mac)
source youtube_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
1. Get your YouTube Data API v3 key from [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Copy `config/.env.template` to the root directory as `.env`
3. Replace `YOUR_API_KEY_HERE` with your actual API key

```bash
# Copy template
cp config/.env.template .env

# Edit .env file and add your API key
API_KEY=your_actual_api_key_here
```

### 5. Run the Application

#### 🎯 Easy Way (Recommended)
```bash
# Use the launcher script
.\run_launcher.ps1  # Windows PowerShell
```

#### 🔧 Manual Way
```bash
# Streamlit (Web Interface)
python -m streamlit run src/youtube_frontend.py

# Gradio (Alternative Web Interface)
python src/youtube_gradio.py

# Console Version
python src/youtube_search.py
```

## 📁 Project Structure

```
youtube-search-app/
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 📄 .gitignore                   # Git ignore rules
├── 📄 .env                         # API key (not tracked by git)
├── 📄 run_launcher.ps1             # Main launcher script
├── 📁 src/                         # Source code
│   ├── 🐍 youtube_search.py        # Core search functionality
│   ├── 🌐 youtube_frontend.py      # Streamlit web interface
│   └── 🎛️ youtube_gradio.py        # Gradio web interface
├── 📁 scripts/                     # Utility scripts
│   ├── 📄 run_frontend.ps1         # Alternative launcher
│   ├── 📄 run_frontend.bat         # Batch launcher
│   └── 🐍 run_with_api_key.py      # API key helper
├── 📁 config/                      # Configuration files
│   └── 📄 .env.template            # Environment template
├── 📁 docs/                        # Documentation
└── 📁 youtube_env/                 # Virtual environment (not tracked)
```

## 🖥️ Interfaces

### 🌐 Streamlit Interface
- **URL**: http://localhost:8501
- **Features**: Modern UI, video thumbnails, interactive controls
- **Best for**: General use, presentation, visual browsing

### 🎛️ Gradio Interface
- **URL**: Auto-opens in browser (usually http://localhost:7860)
- **Features**: Simple layout, text-based results, easy sharing
- **Best for**: Quick searches, API-like usage

### 💻 Console Interface
- **Usage**: Direct terminal output
- **Features**: Scriptable, automation-friendly
- **Best for**: Batch processing, automation scripts

## ⚙️ Configuration Options

### Search Parameters
| Parameter | Options | Description |
|-----------|---------|-------------|
| **Max Results** | 1-10 | Number of videos to return |
| **Duration** | short, medium, long, any | Video length filter |
| **Region** | NL, US, GB, DE, FR, JP, IN, CA, AU | Geographic region |
| **Safe Search** | strict, moderate, none | Content filtering |
| **Sort Order** | relevance, date, rating, viewCount, title | Result ordering |
| **Quality** | any, high, standard | Video definition |
| **Date Range** | Custom dates | Publication date filter |

### Advanced Features
- **Video Embeddable**: Only returns embeddable videos
- **Language**: English language preference
- **Video Type**: Filters for video content only
- **Captions**: Supports caption filtering

## 🔧 Development

### Requirements
- Python 3.8+
- YouTube Data API v3 key
- Internet connection

### Dependencies
```
google-api-python-client==2.183.0
google-auth==2.40.3
google-auth-oauthlib==1.2.2
google-auth-httplib2==0.2.0
streamlit==1.39.0
gradio==5.6.0
python-dotenv==1.0.1
pytest==8.4.2
```

### Getting YouTube API Key
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable "YouTube Data API v3"
4. Go to "Credentials" and create an API key
5. Copy the key to your `.env` file

## 🐛 Troubleshooting

### Common Issues

#### API Key Not Working
```bash
# Check if API key is set
echo $API_KEY  # Linux/Mac
echo $env:API_KEY  # Windows PowerShell

# Verify .env file exists and has correct format
cat .env
```

#### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf youtube_env  # Linux/Mac
Remove-Item youtube_env -Recurse  # Windows

python -m venv youtube_env
# Activate and reinstall packages
```

#### Port Already in Use
```bash
# Kill processes on specific ports
# Streamlit (8501)
netstat -ano | findstr :8501  # Windows
lsof -ti:8501 | xargs kill  # Linux/Mac

# Gradio (7860)
netstat -ano | findstr :7860  # Windows
lsof -ti:7860 | xargs kill  # Linux/Mac
```

#### Package Installation Issues
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v
```

## 📊 Usage Examples

### Streamlit Interface
1. Open http://localhost:8501
2. Enter search term (e.g., "python tutorials")
3. Expand "Advanced Options" for filtering
4. Click "Search Videos"
5. Browse results with thumbnails and direct links

### Console Usage
```python
# Basic search
python src/youtube_search.py

# The script will search for "theory of relativity" by default
# Edit the search_string variable in the file for different queries
```

### API Integration
```python
from src.youtube_search import search_youtube_videos, get_youtube_service

# Initialize service
youtube = get_youtube_service()

# Search with custom parameters
results = search_youtube_videos(
    youtube, 
    "machine learning",
    max_results=10,
    video_duration="medium",
    region_code="US"
)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google YouTube Data API v3
- Streamlit community
- Gradio team
- Python ecosystem contributors

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/youtube-search-app/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/youtube-search-app/discussions)
- 📖 **Documentation**: Check the `docs/` folder for additional guides

---

**Made with ❤️ and Python**