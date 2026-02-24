from crewai import Agent, LLM
from tools import search_news, get_stock_data

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key_env="GEMINI_API_KEY"
)

news_agent = Agent(
    role="Financial News Researcher",
    goal="Find the latest and most relevant news about a stock",
    backstory="You are an expert financial journalist who tracks market news 24/7.",
    tools=[search_news],
    llm=llm,
    verbose=True
)

data_agent = Agent(
    role="Stock Data Analyst",
    goal="Fetch and interpret real-time stock market data",
    backstory="You are a quantitative analyst who specializes in reading stock fundamentals.",
    tools=[get_stock_data],
    llm=llm,
    verbose=True
)

analysis_agent = Agent(
    role="Investment Analyst",
    goal="Analyze news and stock data together to form a view on the stock",
    backstory="You are a senior analyst at a top hedge fund with 15 years of experience.",
    llm=llm,
    verbose=True
)

report_agent = Agent(
    role="Financial Report Writer",
    goal="Write a clean, structured investment research report",
    backstory="You are a professional financial writer who turns complex analysis into clear reports.",
    llm=llm,
    verbose=True
)