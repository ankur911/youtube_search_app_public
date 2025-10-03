#!/bin/bash
# Deployment script for Unix-based systems (Linux/macOS)

echo "🚀 YouTube Search App - Streamlit Deployment Script"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $python_version is installed, but Python $required_version or higher is required."
    exit 1
fi

echo "✅ Python $python_version detected"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating template..."
    echo "API_KEY=your_youtube_api_key_here" > .env
    echo "📝 Please edit .env file and add your YouTube API key"
    echo "   You can get one from: https://console.cloud.google.com/"
fi

# Get the local IP address
if command -v hostname &> /dev/null; then
    local_ip=$(hostname -I | awk '{print $1}' 2>/dev/null || echo "localhost")
else
    local_ip="localhost"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the app:"
echo "1. Make sure you've set your API_KEY in the .env file"
echo "2. Run: streamlit run streamlit_app.py"
echo ""
echo "The app will be available at:"
echo "  🏠 Local: http://localhost:8501"
if [ "$local_ip" != "localhost" ]; then
    echo "  🌐 Network: http://$local_ip:8501"
fi
echo ""
echo "For network access (other devices on same network):"
echo "  streamlit run streamlit_app.py --server.address=0.0.0.0"
echo ""
echo "Happy searching! 🎥"