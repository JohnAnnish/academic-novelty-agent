import os
from langchain.tools import tool
from serpapi import GoogleSearch

@tool
def search_google_scholar(query: str) -> str:
    """Searches Google Scholar for academic papers related to a specific query.
    Returns a string containing the top results with their titles, authors, and summaries.
    Useful for finding literature, related works, and checking novelty."""
    
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "Error: SERPAPI_API_KEY not found in environment."

    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": api_key,
        "num": 5  # Top 5 results to keep context window manageable
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        organic_results = results.get("organic_results", [])
        
        if not organic_results:
            return "No academic papers found for this query."
            
        formatted_results = []
        for result in organic_results:
            title = result.get("title", "No Title")
            authors_info = result.get("publication_info", {}).get("summary", "No Authors")
            snippet = result.get("snippet", "No summary available")
            link = result.get("link", "No Link")
            
            entry = f"Title: {title}\nAuthors/Journal: {authors_info}\nSummary: {snippet}\nLink: {link}\n---"
            formatted_results.append(entry)
            
        return "\n".join(formatted_results)
    
    except Exception as e:
        return f"An error occurred while searching: {e}"

if __name__ == "__main__":
    # Quick test to make sure it works standalone
    from dotenv import load_dotenv
    load_dotenv()
    print("Testing Google Scholar Search Tool...")
    # This invokes the tool exactly as the LLM will
    print(search_google_scholar.invoke({"query": "FCM segmentation EfficientNet XGBoost Leukemia"}))
