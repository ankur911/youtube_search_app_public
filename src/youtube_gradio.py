import gradio as gr
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_youtube_service():
    """Initialize YouTube API service"""
    api_key = os.getenv("API_KEY")
    if not api_key:
        return None, "ERROR: API_KEY environment variable is not set! Please set your YouTube Data API v3 key in your .env file"
    
    try:
        return build("youtube", "v3", developerKey=api_key), None
    except Exception as e:
        return None, f"Error initializing YouTube service: {str(e)}"

def search_youtube_videos(search_string, max_results=5, video_duration="short", region_code="NL", safe_search="strict", order="relevance"):
    """Search for YouTube videos and return formatted results"""
    if not search_string.strip():
        return "Please enter a search term."
    
    youtube, error = get_youtube_service()
    if error:
        return error
    
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
            videoDefinition='high',
            publishedAfter='2024-01-01T00:00:00Z',
            publishedBefore='2025-07-31T23:59:59Z',
            order=order
        )
        
        response = request.execute()
        videos = response['items']
        
        if not videos:
            return "No videos found. Try different search terms."
        
        # Format the output
        output_text = f"🎥 Search results for: {search_string}\n"
        output_text += "=" * 50 + "\n\n"
        
        for i, item in enumerate(videos, 1):
            title = item['snippet']['title']
            channel = item['snippet']['channelTitle']
            video_id = item['id']['videoId']
            published = item['snippet']['publishedAt']
            description = item['snippet']['description']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            output_text += f"{i}. 📺 Title: {title}\n"
            output_text += f"   👤 Channel: {channel}\n"
            output_text += f"   📅 Published: {published[:10]}\n"
            output_text += f"   🔗 URL: {video_url}\n"
            
            # Add description preview
            if description:
                desc_preview = description[:100] + "..." if len(description) > 100 else description
                output_text += f"   📝 Description: {desc_preview}\n"
            
            output_text += "-" * 30 + "\n\n"
        
        return output_text
    
    except Exception as e:
        return f"Error searching YouTube: {str(e)}"

# Create Gradio interface
def create_interface():
    with gr.Blocks(title="YouTube Search App", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🎥 YouTube Video Search")
        gr.Markdown("Search for YouTube videos and get direct links!")
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## 🔍 Search")
                search_input = gr.Textbox(
                    label="Search Term",
                    placeholder="e.g., theory of relativity",
                    info="Enter keywords to search for YouTube videos"
                )
                
                # Advanced options
                with gr.Accordion("⚙️ Advanced Options", open=False):
                    with gr.Row():
                        max_results = gr.Slider(
                            label="Number of Results",
                            minimum=1,
                            maximum=10,
                            value=5,
                            step=1
                        )
                        video_duration = gr.Dropdown(
                            label="Video Duration",
                            choices=["short", "medium", "long", "any"],
                            value="short",
                            info="short: <4min, medium: 4-20min, long: >20min"
                        )
                    
                    with gr.Row():
                        region_code = gr.Dropdown(
                            label="Region Code",
                            choices=["NL", "US", "GB", "DE", "FR", "JP", "IN", "CA", "AU"],
                            value="NL",
                            info="Filter results by region"
                        )
                        safe_search = gr.Dropdown(
                            label="Safe Search",
                            choices=["strict", "moderate", "none"],
                            value="strict",
                            info="Filter explicit content"
                        )
                    
                    order = gr.Dropdown(
                        label="Sort Order",
                        choices=["relevance", "date", "rating", "viewCount", "title"],
                        value="relevance",
                        info="How to sort the search results"
                    )
                
                search_button = gr.Button("Search Videos", variant="primary")
            
            with gr.Column(scale=2):
                gr.Markdown("## 📺 Results")
                output = gr.Textbox(
                    label="Search Results",
                    placeholder="Enter a search term and click 'Search Videos' to get started!",
                    lines=20,
                    max_lines=30,
                    show_copy_button=True
                )
        
        # Connect the search function
        search_button.click(
            fn=search_youtube_videos,
            inputs=[search_input, max_results, video_duration, region_code, safe_search, order],
            outputs=output
        )
        
        # Also trigger search on Enter key
        search_input.submit(
            fn=search_youtube_videos,
            inputs=[search_input, max_results, video_duration, region_code, safe_search, order],
            outputs=output
        )
        
        gr.Markdown("---")
        gr.Markdown("Made with ❤️ using Gradio and YouTube Data API v3")
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        share=False,  # Set to True if you want to share publicly
        server_name="127.0.0.1",
        server_port=7860
    )