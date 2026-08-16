from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()


# https://www.tavily.com/ 
# Signup and login, On dashboard- > under api keys you will see the default key.
# Use that or click on + to create new one. Then save it in .env file

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
client = TavilyClient(
    api_key=TAVILY_API_KEY
) if TAVILY_API_KEY else None

# test it
#################################
# response = client.search(
    # query="Best hotels in Dubai"
# )

# print(response)

####################################



def tavily_search(query):
    if client is None:
        return (
            "Tavily API key is not configured. Add TAVILY_API_KEY to your .env file "
            "to enable live routing, hotel, and travel research."
        )

    response = client.search(
        query=query,
        max_results=5
    )

    results = []
    items = response.get("results", []) if isinstance(response, dict) else []

    for i, r in enumerate(items, 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    if not results:
        return "No transport or hotel results were returned for this query."

    return "\n\n".join(results)