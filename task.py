from crewai import Task
from agents import news_agent, data_agent, analysis_agent, report_agent

def create_tasks(ticker: str):

    news_task = Task(
        description=f"Search and summarize the latest financial news for {ticker} stock.",
        expected_output="A bullet point summary of the 5 most relevant recent news items about the stock.",
        agent=news_agent
    )

    data_task = Task(
        description=f"Fetch the current stock data and key financial metrics for {ticker}.",
        expected_output="A structured summary of the stock's current price, PE ratio, market cap, 52 week high/low, revenue and profit margin.",
        agent=data_agent
    )

    analysis_task = Task(
        description=f"Using the news and stock data provided, analyze the overall health and outlook of {ticker}.",
        expected_output="A 2-3 paragraph analysis covering strengths, risks, and overall sentiment.",
        agent=analysis_agent,
        context=[news_task, data_task]
    )

    report_task = Task(
        description=f"Write a professional investment research report for {ticker} based on all the analysis.",
        expected_output="""A structured report with the following sections:
        - Executive Summary
        - Latest News
        - Key Financial Metrics
        - Analysis
        - Conclusion & Recommendation""",
        agent=report_agent,
        context=[news_task, data_task, analysis_task]
    )

    return [news_task, data_task, analysis_task, report_task]