"""
Bing Search Skill Entry Point
This module provides the interface between OpenClaw and the Bing Search API
"""
from .bing_search import search, get_news


def bing_web_search(query: str, count: int = 10, market: str = "en-US", safe_search: str = "Moderate"):
    """
    Perform a web search using Bing API
    
    Args:
        query: Search query string
        count: Number of results to return (default 10)
        market: Market code for localization (default en-US)
        safe_search: Safe search setting (Off, Moderate, Strict)
    
    Returns:
        Dictionary containing search results
    """
    return search(query=query, count=count, market=market, safe_search=safe_search)


def bing_news_search(query: str = "", count: int = 10, market: str = "en-US"):
    """
    Get news articles using Bing News API
    
    Args:
        query: News topic to search for (empty for general news)
        count: Number of results to return
        market: Market code for localization
    
    Returns:
        Dictionary containing news articles
    """
    return get_news(query=query, count=count, market=market)


# Export the functions
__all__ = ['bing_web_search', 'bing_news_search']