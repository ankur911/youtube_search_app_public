import streamlit as st
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from datetime import date

# Load environment variables
load_dotenv()

def get_youtube_service():
    """Initialize YouTube API service"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        st.error("ERROR: API_KEY environment variable is not set!")
        st.info("Please set your YouTube Data API v3 key in your .env file")
        st.stop()
    
    return build("youtube", "v3", developerKey=api_key)

def search_youtube_videos(youtube, search_string, max_results=5, video_duration="short", region_code="NL", safe_search="strict", order="relevance", video_definition="any", published_after="2024-01-01T00:00:00Z", published_before="2025-07-31T23:59:59Z"):
    """Search for YouTube videos with dynamic parameters"""
    try:
        request = youtube.search().list(
            part="snippet",
            maxResults=max_results,
            q=search_string,
            videoDuration=video_duration,
            videoEmbeddable="true",
            type="video",
            regionCode=region_code,
            relevanceLanguage='en',
            safeSearch=safe_search,
            videoCaption='any',
            videoDefinition=video_definition,
            publishedAfter=published_after,
            publishedBefore=published_before,
            order=order
        )
        
        response = request.execute()
        return response['items']
    
    except Exception as e:
        st.error(f"Error searching YouTube: {str(e)}")
        return []

def main():
    st.set_page_config(
        page_title="YouTube Search App",
        page_icon="🎥",
        layout="wide"
    )
    
    st.title("🎥 YouTube Video Search")
    st.markdown("Search for YouTube videos and get direct links!")
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🔍 Search")
        
        # Search input box
        search_string = st.text_input(
            "Enter your search term:",
            placeholder="e.g., theory of relativity",
            help="Enter keywords to search for YouTube videos"
        )
        
        # Search button
        search_button = st.button("Search Videos", type="primary")
        
        # Additional search options (optional)
        with st.expander("Advanced Options"):
            col_a, col_b = st.columns(2)
            
            with col_a:
                max_results = st.slider("Number of results", 1, 10, 5)
                video_duration = st.selectbox(
                    "Video Duration",
                    ["short", "medium", "long", "any"],
                    index=0,
                    help="short: <4min, medium: 4-20min, long: >20min"
                )
                region_code = st.selectbox(
                    "Region Code",
                    ["NL", "US", "GB", "DE", "FR", "JP", "IN", "CA", "AU"],
                    index=0,
                    help="Filter results by region"
                )
            
            with col_b:
                safe_search = st.selectbox(
                    "Safe Search",
                    ["strict", "moderate", "none"],
                    index=0,
                    help="Filter explicit content"
                )
                order = st.selectbox(
                    "Sort Order",
                    ["relevance", "date", "rating", "viewCount", "title"],
                    index=0,
                    help="How to sort the search results"
                )
                video_definition = st.selectbox(
                    "Video Quality",
                    ["any", "high", "standard"],
                    index=0,
                    help="Filter by video definition"
                )
            
            # Date range
            st.subheader("📅 Date Range")
            date_col1, date_col2 = st.columns(2)
            with date_col1:
                published_after = st.date_input(
                    "Published After",
                    value=date(2024, 1, 1),
                    help="Show videos published after this date"
                )
            with date_col2:
                published_before = st.date_input(
                    "Published Before", 
                    value=date(2025, 7, 31),
                    help="Show videos published before this date"
                )
    
    with col2:
        st.subheader("📺 Search Results")
        
        # Output area
        if search_button and search_string:
            with st.spinner("Searching YouTube..."):
                youtube = get_youtube_service()
                
                # Convert dates to ISO format
                published_after_iso = f"{published_after}T00:00:00Z"
                published_before_iso = f"{published_before}T23:59:59Z"
                
                videos = search_youtube_videos(
                    youtube, 
                    search_string, 
                    max_results=max_results,
                    video_duration=video_duration,
                    region_code=region_code,
                    safe_search=safe_search,
                    order=order,
                    video_definition=video_definition,
                    published_after=published_after_iso,
                    published_before=published_before_iso
                )
                
                if videos:
                    st.success(f"Found {len(videos)} videos for: **{search_string}**")
                    
                    # Display results
                    for i, item in enumerate(videos, 1):
                        title = item['snippet']['title']
                        channel = item['snippet']['channelTitle']
                        video_id = item['id']['videoId']
                        published = item['snippet']['publishedAt']
                        description = item['snippet']['description']
                        thumbnail_url = item['snippet']['thumbnails']['medium']['url']
                        video_url = f"https://www.youtube.com/watch?v={video_id}"
                        
                        # Create a card-like display for each video
                        with st.container():
                            st.markdown("---")
                            
                            # Create columns for thumbnail and info
                            thumb_col, info_col = st.columns([1, 3])
                            
                            with thumb_col:
                                st.image(thumbnail_url, width=150)
                            
                            with info_col:
                                st.markdown(f"**{i}. {title}**")
                                st.markdown(f"📺 **Channel:** {channel}")
                                st.markdown(f"📅 **Published:** {published[:10]}")
                                st.markdown(f"🔗 **URL:** {video_url}")
                                
                                # Add a clickable link
                                st.markdown(f"[▶️ Watch Video]({video_url})")
                                
                                # Show description (truncated)
                                if description:
                                    desc_preview = description[:200] + "..." if len(description) > 200 else description
                                    with st.expander("📝 Description"):
                                        st.write(desc_preview)
                
                else:
                    st.warning("No videos found. Try different search terms.")
        
        elif search_button and not search_string:
            st.warning("Please enter a search term.")
        
        else:
            st.info("👆 Enter a search term and click 'Search Videos' to get started!")
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit and YouTube Data API v3")

if __name__ == "__main__":
    main()