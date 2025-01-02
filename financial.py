from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.tools.duckduckgo as ddg_module
print(dir(ddg_module))
import phi.utils as utils
print(dir(utils))

web_search_agent = Agent(
    name = "WEB Search Agent",
    role = "Search web for the information",
    model = Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools = [DuckDuckGo()],
    instructions=['Always include sources'],
    show_tools_calls = True,
    markdown=True,
)

## Financial Agent
finance_agent =Agent(
    name='Financial AI Agent',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)
        ],
    instructions=["Use tables to  display the data"],
    show_tool_calls=True,
    markdown=True,
    
)

multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    instructions=['Always include sources',"Use tables to  display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analysis recommedation and share the latest news for NVDA", stream=True)
