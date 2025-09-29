from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import os
import pytest
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")

# Check if API key is set
if not api_key:
    print("ERROR: API_KEY environment variable is not set!")
    print("Please set your YouTube Data API v3 key:")
    print("Option 1: $env:API_KEY = 'YOUR_ACTUAL_API_KEY'")
    print("Option 2: Use the run_with_api_key.py script")
    print("Get your API key from: https://console.cloud.google.com/apis/credentials")
    exit(1)
# service_account_file = os.getenv("SERVICE_ACCOUNT_FILE")
# scopes = ["https://www.googleapis.com/auth/cloud-platform"]
# project_id = os.getenv("PROJECT_ID")

# credentials = service_account.Credentials.from_service_account_file(
#     service_account_file, scopes=scopes
# )

# youtube = build("youtube", "v3", credentials=credentials)
youtube = build("youtube", "v3", developerKey=api_key)

search_string = "theory of relativity"
request = youtube.search().list(
    part="snippet",  # Note: statistics is not available for search, only for videos
    maxResults=5,
    q=search_string,
    videoDuration="short",  # any, long (> 20 minutes), medium (< 20 minutes), short (< 4 minutes)
    videoEmbeddable="true", #any
    type="video",  # Specify that we want videos
    # location='37.42307,-122.08427',
    # locationRadius='1000m',
    regionCode='NL',
    relevanceLanguage='en',
    safeSearch='strict', # none, moderate, strict
    videoCaption='any', # none, closedCaption, any
    # videoCategoryId='27', # 1 Film & Animation, 2 Autos & Vehicles
    videoDefinition='high', # any, high, standard
    # videoDimension='2d', # 2d, 3d, any
    publishedAfter='2024-01-01T00:00:00Z',
    publishedBefore='2025-07-31T23:59:59Z',
    order='relevance'
    # ,'rating','viewCount'
    #   order: string, Sort order of the results.
    # Allowed values
    #   searchSortUnspecified - 
    #   date - Resources are sorted in reverse chronological order based on the date they were created.
    #   rating - Resources are sorted from highest to lowest rating.
    #   viewCount - Resources are sorted from highest to lowest number of views.
    #   relevance - Resources are sorted based on their relevance to the search query. This is the default value for this parameter.
    #   title - Resources are sorted alphabetically by title.
    #   videoCount - Channels are sorted in descending order of their number of uploaded videos.

)

# Execute the request
response = request.execute()

# Print the results
print(f"Search results for: {search_string}")
print("=" * 50)

for item in response['items']:
    print(item)
    title = item['snippet']['title']
    channel = item['snippet']['channelTitle']
    video_id = item['id']['videoId']
    published = item['snippet']['publishedAt']
    channelTitle = item['snippet']['channelTitle']
    description = item['snippet']['description']
    
    print(f"Title: {title}")
    print(f"Channel: {channel}")
    print(f"ChannelTitle: {channelTitle}")
    print(f"Description: {description}")
    print(f"Video ID: {video_id}")
    print(f"Published: {published}")
    print(f"URL: https://www.youtube.com/watch?v={video_id}")
    print("-" * 30)