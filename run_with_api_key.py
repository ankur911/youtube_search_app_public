import os
import sys

def main():
    # You can set your API key here temporarily for testing
    # Replace 'YOUR_API_KEY_HERE' with your actual YouTube Data API v3 key
    api_key = "YOUR_API_KEY_HERE"
    
    if api_key == "YOUR_API_KEY_HERE":
        print("Please replace 'YOUR_API_KEY_HERE' with your actual YouTube Data API v3 key")
        print("Get your API key from: https://console.cloud.google.com/apis/credentials")
        print("1. Go to Google Cloud Console")
        print("2. Create a new project or select existing one")
        print("3. Enable YouTube Data API v3")
        print("4. Create credentials (API key)")
        print("5. Replace the placeholder in this script")
        return
    
    # Set the environment variable
    os.environ["API_KEY"] = api_key
    
    # Import and run the test
    try:
        import youtube_search
        print("YouTube API search completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your API key is valid and the YouTube Data API v3 is enabled.")

if __name__ == "__main__":
    main()