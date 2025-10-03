import streamlit as st
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from datetime import date

# Load environment variables
load_dotenv()

def get_youtube_service():
    """Initialize YouTube API service with deployment-friendly API key handling"""
    # Try to get API key from Streamlit secrets first (for cloud deployment)
    api_key = None
    try:
        api_key = st.secrets["API_KEY"]
    except (KeyError, FileNotFoundError):
        # Fallback to environment variable (for local development)
        api_key = os.getenv("API_KEY")
    
    if not api_key:
        st.error("ERROR: API_KEY is not configured!")
        st.info("""
        Please configure your YouTube Data API v3 key:
        
        **For Streamlit Cloud deployment:**
        - Add API_KEY to your app's secrets in the Streamlit Cloud dashboard
        
        **For local development:**
        - Set API_KEY in your .env file
        - Or set it as an environment variable
        
        **For other cloud platforms:**
        - Set API_KEY as an environment variable in your deployment settings
        """)
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
        page_title="YouTube Search App - Deployed",
        page_icon="🎥",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state for video display and search results
    if 'video_states' not in st.session_state:
        st.session_state.video_states = {}
    if 'search_results' not in st.session_state:
        st.session_state.search_results = []
    if 'last_search_term' not in st.session_state:
        st.session_state.last_search_term = ""
    
    # Custom CSS for better video embedding and deployment styling
    st.markdown("""
    <style>
    .video-container {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
    }
    .video-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .video-title {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .deployment-badge {
        position: fixed;
        top: 10px;
        right: 10px;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 12px;
        z-index: 1000;
    }
    .main-header {
        text-align: center;
        margin-bottom: 30px;
    }
    .feature-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Deployment badge
    st.markdown('<div class="deployment-badge">🚀 Deployed Version</div>', unsafe_allow_html=True)
    
    # Main header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🎥 YouTube Video Search")
    st.markdown("**Search for YouTube videos and play them directly in the app!**")
    st.markdown("🌐 *This is the deployment-ready version accessible from anywhere*")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add deployment info in sidebar
    with st.sidebar:
        st.markdown("### 🚀 Deployment Info")
        st.info("""
        This is the deployment version of the YouTube Search App.
        
        **Features:**
        - ☁️ Cloud-ready deployment
        - 🔑 Multiple API key sources
        - 📱 Mobile-friendly interface
        - 🌐 Cross-platform compatibility
        """)
        
        st.markdown("### 📋 How to Use")
        st.markdown("""
        1. Enter your search term
        2. Adjust settings (optional)
        3. Click "Search Videos"
        4. Click "▶️ Play Video" to watch
        """)
        
        st.markdown("### 🔧 Technical Details")
        st.code(f"""
        Platform: Streamlit
        Python: {os.sys.version.split()[0]}
        API: YouTube Data API v3
        """)
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.subheader("🔍 Search Configuration")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Search input box
        search_string = st.text_input(
            "Enter your search term:",
            placeholder="e.g., theory of relativity, cooking tutorial, music",
            help="Enter keywords to search for YouTube videos"
        )
        
        # Search button
        search_button = st.button("🔍 Search Videos", type="primary", use_container_width=True)
        
        # Clear results button (only show if there are results)
        if st.session_state.search_results:
            if st.button("🗑️ Clear Results", type="secondary", use_container_width=True):
                st.session_state.search_results = []
                st.session_state.last_search_term = ""
                # Clear all video states
                for key in list(st.session_state.keys()):
                    if key.startswith("show_video_"):
                        del st.session_state[key]
                st.rerun()
        
        # Additional search options (optional)
        with st.expander("⚙️ Advanced Options"):
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
            with st.spinner("🔍 Searching YouTube videos..."):
                try:
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
                    
                    # Store results in session state
                    st.session_state.search_results = videos
                    st.session_state.last_search_term = search_string
                    
                except Exception as e:
                    st.error(f"Failed to initialize YouTube service: {str(e)}")
                    st.info("Please check your API key configuration.")
        
        # Display results from session state (if any)
        if st.session_state.search_results:
            videos = st.session_state.search_results
            search_string = st.session_state.last_search_term
            
            if videos:
                st.success(f"✅ Found {len(videos)} videos for: **{search_string}**")
                
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
                            
                            # Create button columns
                            btn_col1, btn_col2 = st.columns([1, 1])
                            
                            with btn_col1:
                                # Add embedded video player
                                play_button_key = f"play_video_{i}_{video_id}"
                                if st.button(f"▶️ Play Video", key=play_button_key, type="secondary"):
                                    st.session_state[f"show_video_{video_id}"] = True
                                    st.rerun()
                            
                            with btn_col2:
                                # Add external link
                                st.link_button("🔗 Open in YouTube", video_url)
                            
                            # Show embedded video if play button was clicked
                            if st.session_state.get(f"show_video_{video_id}", False):
                                st.markdown('<div class="video-title">🎬 Now Playing:</div>', unsafe_allow_html=True)
                                # Embed YouTube video using iframe with responsive design
                                embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&rel=0&modestbranding=1"
                                st.markdown(f"""
                                <div class="video-container">
                                    <iframe 
                                    src="{embed_url}" 
                                    frameborder="0" 
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                                    allowfullscreen>
                                    </iframe>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Add a button to hide the video
                                hide_button_key = f"hide_video_{i}_{video_id}"
                                if st.button("❌ Close Video", key=hide_button_key):
                                    st.session_state[f"show_video_{video_id}"] = False
                                    st.rerun()
                            
                            # Show description (truncated)
                            if description:
                                desc_preview = description[:200] + "..." if len(description) > 200 else description
                                with st.expander("📝 Description"):
                                    st.write(desc_preview)
            
            else:
                st.warning("⚠️ No videos found. Try different search terms or adjust your filters.")
        
        elif search_button and not search_string:
            st.warning("⚠️ Please enter a search term.")
        
        else:
            st.info("👆 Enter a search term and click 'Search Videos' to get started!")
            
            # Show example searches
            st.markdown("### 💡 Example searches:")
            example_col1, example_col2 = st.columns(2)
            with example_col1:
                st.markdown("""
                - 🧠 "machine learning tutorial"
                - 🍳 "easy cooking recipes"
                - 🎵 "relaxing music"
                """)
            with example_col2:
                st.markdown("""
                - 🚀 "space exploration"
                - 💻 "programming for beginners"
                - 🎨 "digital art techniques"
                """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        Made with ❤️ using Streamlit and YouTube Data API v3<br>
        🚀 <strong>Deployment Ready</strong> | 🌐 <strong>Cross-Platform Compatible</strong>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()