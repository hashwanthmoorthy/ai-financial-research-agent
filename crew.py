from crewai import Crew, Process
from agents import news_agent, data_agent, analysis_agent, report_agent
from task import create_tasks
from dotenv import load_dotenv

load_dotenv()

def run_research(ticker: str):
    tasks = create_tasks(ticker)

    crew = Crew(
        agents=[news_agent, data_agent, analysis_agent, report_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g. AAPL): ").upper()
    result = run_research(ticker)
    print("\n\n==================== FINAL REPORT ====================")
    print(result)