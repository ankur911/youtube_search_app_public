# Make sure you're in the virtual environment
.\youtube_env\Scripts\Activate.ps1

# Option 1: Set environment variable and run test.py directly
$env:API_KEY = "YOUR_ACTUAL_API_KEY"
python test.py

# Option 2: Edit run_with_api_key.py and run it
python run_with_api_key.py

# Streamlit (currently running)
python -m streamlit run youtube_frontend.py

# Gradio
python youtube_gradio.py

# Original console version
python youtube_search.py

# PowerShell
.\run_frontend.ps1

# OR Command Prompt
run_frontend.bat