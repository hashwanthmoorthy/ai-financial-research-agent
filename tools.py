import yfinance as yf
from duckduckgo_search import DDGS
from crewai.tools import tool

@tool("Search Financial News")
def search_news(ticker: str) -> str:
    """Search latest financial news for a given stock ticker."""
    with DDGS() as ddgs:
        results = ddgs.text(f"{ticker} stock news 2024", max_results=5)
        news = ""
        for r in results:
            news += f"Title: {r['title']}\nSummary: {r['body']}\n\n"
        return news if news else "No news found."

@tool("Get Stock Data")
def get_stock_data(ticker: str) -> str:
    """Fetch real-time stock data for a given ticker."""
    stock = yf.Ticker(ticker)
    info = stock.info
    data = f"""
    Company: {info.get('longName', 'N/A')}
    Current Price: ${info.get('currentPrice', 'N/A')}
    Market Cap: ${info.get('marketCap', 'N/A'):,}
    PE Ratio: {info.get('trailingPE', 'N/A')}
    52 Week High: ${info.get('fiftyTwoWeekHigh', 'N/A')}
    52 Week Low: ${info.get('fiftyTwoWeekLow', 'N/A')}
    Revenue: ${info.get('totalRevenue', 'N/A')}
    Profit Margin: {info.get('profitMargins', 'N/A')}
    """
    return data