from agents import Agent, Runner, function_tool
from connection import config

# ---- Function tool: BTC to PKR ----
@function_tool
def btc_to_pkr():
    return 'Today 1 BTC to PKR is Rs 32790413.22'

# ---- Function tool: ETH to PKR ----
@function_tool
def eth_to_pkr():
    return 'Today 1 ETH to PKR is Rs 1210790.47'

# ---- Agent ----
crypto_agent = Agent(
    name = 'Crypto Data Agent',
    instructions = """
        You are a helpful crypto assistant. 
        Your task is to tell user about cryptocurrency exchange rates (BTC, ETH to PKR).
    """,
    tools = [btc_to_pkr, eth_to_pkr]
)

# ---- Run Agent ----
result = Runner.run_sync(
    crypto_agent,
    'What is BTC to PKR today?',
    run_config=config
)

print(result.final_output)


