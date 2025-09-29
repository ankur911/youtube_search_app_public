# 📚 API Reference

## YouTube Search Functions

### `get_youtube_service()`

Initializes the YouTube API service.

**Returns:**
- `googleapiclient.discovery.Resource`: YouTube API service object

**Raises:**
- `Exception`: If API key is not set or invalid

### `search_youtube_videos(youtube, search_string, **kwargs)`

Searches for YouTube videos with specified parameters.

**Parameters:**
- `youtube` (Resource): YouTube API service object
- `search_string` (str): Search query
- `max_results` (int, optional): Number of results (1-10). Default: 5
- `video_duration` (str, optional): Duration filter. Options: "short", "medium", "long", "any". Default: "short"
- `region_code` (str, optional): Region code (e.g., "US", "NL"). Default: "NL"
- `safe_search` (str, optional): Safe search level. Options: "strict", "moderate", "none". Default: "strict"
- `order` (str, optional): Sort order. Options: "relevance", "date", "rating", "viewCount", "title". Default: "relevance"
- `video_definition` (str, optional): Video quality. Options: "any", "high", "standard". Default: "any"
- `published_after` (str, optional): ISO date string. Default: "2024-01-01T00:00:00Z"
- `published_before` (str, optional): ISO date string. Default: "2025-07-31T23:59:59Z"

**Returns:**
- `list`: List of video items from YouTube API

**Example:**
```python
youtube = get_youtube_service()
videos = search_youtube_videos(
    youtube, 
    "python tutorials",
    max_results=10,
    video_duration="medium",
    region_code="US"
)
```

## Response Format

Each video item contains:

```python
{
    'id': {
        'videoId': 'string'
    },
    'snippet': {
        'title': 'string',
        'description': 'string',
        'channelTitle': 'string',
        'publishedAt': 'datetime_string',
        'thumbnails': {
            'default': {'url': 'string'},
            'medium': {'url': 'string'},
            'high': {'url': 'string'}
        }
    }
}
```

## Error Handling

### Common Errors

#### Invalid API Key
```
google.auth.exceptions.DefaultCredentialsError
```
**Solution:** Check your .env file and API key

#### Quota Exceeded
```
googleapiclient.errors.HttpError: 403 quotaExceeded
```
**Solution:** Wait for quota reset or increase limits

#### Invalid Parameters
```
googleapiclient.errors.HttpError: 400 Bad Request
```
**Solution:** Check parameter values and types

## Configuration Options

### Video Duration Options
- `"short"`: < 4 minutes
- `"medium"`: 4-20 minutes  
- `"long"`: > 20 minutes
- `"any"`: No duration filter

### Region Codes
- `"US"`: United States
- `"GB"`: United Kingdom
- `"DE"`: Germany
- `"FR"`: France
- `"JP"`: Japan
- `"IN"`: India
- `"CA"`: Canada
- `"AU"`: Australia
- `"NL"`: Netherlands

### Safe Search Levels
- `"strict"`: Strict filtering
- `"moderate"`: Moderate filtering
- `"none"`: No filtering

### Sort Orders
- `"relevance"`: Most relevant first
- `"date"`: Newest first
- `"rating"`: Highest rated first
- `"viewCount"`: Most viewed first
- `"title"`: Alphabetical order

## Rate Limits

- **Daily Quota**: 10,000 units (free tier)
- **Search Cost**: ~100 units per request
- **Effective Searches**: ~100 per day (free tier)

## Best Practices

1. **Cache Results**: Store results to avoid repeated API calls
2. **Batch Requests**: Combine multiple searches when possible
3. **Monitor Quota**: Track API usage in Google Cloud Console
4. **Error Handling**: Always handle API exceptions
5. **Parameter Validation**: Validate inputs before API calls