"""
Streamlit App Entry Point for YouTube Search Application

This is the main entry point for the Streamlit app deployment.
It imports and runs the deployment-optimized YouTube frontend application.
"""

import sys
import os

# Add the src directory to the Python path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the deployment-optimized application
from youtube_frontend_deploy import main

if __name__ == "__main__":
    main()