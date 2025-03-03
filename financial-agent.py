from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information",
    model = Groq(id="llama3-8b-8192"),
    tools=[DuckDuckGo()],
    instructions = "Ensure to include sources",
    show_tool_calls = True,
    markdown = True

)

financial_agent = Agent(
    name = "Financial agent",
    model = Groq(id="llama3-8b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True
)

multi_ai_agent = Agent(
    model = Groq(id='llama-3.1-8b-instant'),
    team=[web_search_agent,financial_agent],
    instructions = ["Ensure to include sources","Format your response using markdown and use tables to display data where possible."] 
 )

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Microsoft",stream=True)
