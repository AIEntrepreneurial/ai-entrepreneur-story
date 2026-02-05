# Bing Search Skill for OpenClaw

This skill provides web search functionality using Microsoft's Bing Search API. It allows OpenClaw to perform web searches and retrieve relevant results.

## Features

- Web search using Bing Search API
- News search using Bing News API
- Configurable result count
- Localization support
- Safe search filtering

## Requirements

- Bing Search API key from [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/bing-web-search-api/)

## Installation

1. Obtain a Bing Search API key from Azure Cognitive Services
2. Set the `BING_SEARCH_API_KEY` environment variable with your API key
3. Install the skill in your OpenClaw instance

## Configuration

Set the following environment variable:

```bash
BING_SEARCH_API_KEY=your_bing_api_key_here
```

## Functions

### `bing_web_search`

Performs a web search using Bing Search API.

Parameters:
- `query` (string, required): Search query string
- `count` (integer, optional): Number of results to return (default: 10)
- `market` (string, optional): Market code for localization (default: "en-US")
- `safe_search` (string, optional): Safe search setting (Off, Moderate, Strict; default: "Moderate")

Example:
```python
results = bing_web_search(query="Python programming tutorials", count=5)
```

### `bing_news_search`

Retrieves news articles using Bing News API.

Parameters:
- `query` (string, optional): News topic to search for (empty for general news)
- `count` (integer, optional): Number of results to return (default: 10)
- `market` (string, optional): Market code for localization (default: "en-US")

Example:
```python
news = bing_news_search(query="technology", count=5)
```

## Usage Examples

### Basic Web Search
```python
# Search for Python programming resources
results = bing_web_search(query="Python programming")
for result in results['results']:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['snippet']}")
    print("---")
```

### News Search
```python
# Get latest technology news
tech_news = bing_news_search(query="technology", count=5)
for article in tech_news['results']:
    print(f"Title: {article['title']}")
    print(f"URL: {article['url']}")
    print(f"Published: {article['date_published']}")
    print("---")
```

## Error Handling

The skill will raise appropriate exceptions if:
- The BING_SEARCH_API_KEY environment variable is not set
- There are issues connecting to the Bing API
- Invalid parameters are provided

## Rate Limits

Be aware of Bing Search API rate limits. The free tier includes a limited number of transactions per month. Check the [official documentation](https://azure.microsoft.com/pricing/details/cognitive-services/search-api/) for current limits.