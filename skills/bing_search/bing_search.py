"""
Bing Web Search Skill
Implements web search functionality using Microsoft Bing Search API
"""
import os
import json
import requests
from typing import Dict, Any, Optional


def search(query: str, count: int = 10, market: str = "en-US", safe_search: str = "Moderate") -> Dict[str, Any]:
    """
    Perform a web search using Bing Search API
    
    Args:
        query: Search query string
        count: Number of results to return (default 10)
        market: Market code for localization (default en-US)
        safe_search: Safe search setting (Off, Moderate, Strict)
    
    Returns:
        Dictionary containing search results
    """
    # Get API key from environment variable
    api_key = os.getenv("BING_SEARCH_API_KEY")
    if not api_key:
        raise ValueError("BING_SEARCH_API_KEY environment variable is not set")
    
    # Bing Search API endpoint
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    
    # Request headers
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }
    
    # Request parameters
    params = {
        "q": query,
        "count": count,
        "mkt": market,
        "safesearch": safe_search
    }
    
    # Make the API request
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()  # Raise exception for bad status codes
    
    # Parse JSON response
    data = response.json()
    
    # Extract relevant information from response
    results = {
        "query": query,
        "total_matches": data.get("totalEstimatedMatches", 0),
        "results": []
    }
    
    # Process web pages results
    if "webPages" in data:
        for result in data["webPages"]["value"]:
            result_item = {
                "title": result.get("name"),
                "url": result.get("url"),
                "snippet": result.get("snippet"),
                "display_url": result.get("displayUrl")
            }
            results["results"].append(result_item)
    
    return results


def get_news(query: str = "", count: int = 10, market: str = "en-US") -> Dict[str, Any]:
    """
    Get news articles using Bing News API
    
    Args:
        query: News topic to search for (empty for general news)
        count: Number of results to return
        market: Market code for localization
    
    Returns:
        Dictionary containing news articles
    """
    # Get API key from environment variable
    api_key = os.getenv("BING_SEARCH_API_KEY")
    if not api_key:
        raise ValueError("BING_SEARCH_API_KEY environment variable is not set")
    
    # Bing News API endpoint
    news_url = "https://api.bing.microsoft.com/v7.0/news/search"
    
    # Request headers
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }
    
    # Request parameters
    params = {
        "q": query if query else "general",
        "count": count,
        "mkt": market
    }
    
    # Make the API request
    response = requests.get(news_url, headers=headers, params=params)
    response.raise_for_status()
    
    # Parse JSON response
    data = response.json()
    
    # Extract relevant information
    results = {
        "query": query if query else "general",
        "total_matches": data.get("totalEstimatedMatches", 0),
        "results": []
    }
    
    # Process news articles
    if "value" in data:
        for article in data["value"]:
            article_item = {
                "title": article.get("name"),
                "url": article.get("url"),
                "snippet": article.get("description"),
                "date_published": article.get("datePublished"),
                "provider": article.get("provider")[0].get("name") if article.get("provider") else None
            }
            results["results"].append(article_item)
    
    return results


# Example usage
if __name__ == "__main__":
    # Example: Search for "Python programming"
    try:
        search_results = search("Python programming", count=5)
        print(f"Found {len(search_results['results'])} results:")
        for i, result in enumerate(search_results['results'], 1):
            print(f"{i}. {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Snippet: {result['snippet']}")
            print()
    except Exception as e:
        print(f"Error performing search: {e}")