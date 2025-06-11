from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

# llm = ChatOpenAI(model="gpt-3")
# llm = ChatOllama(model="qwen3:4b")
llm = ChatOllama(model="qwen3:8b")
# llm = ChatOllama(model="devstral:latest")
# llm = ChatOllama(model="deepseek-r1:8b")


initial_actions = [
	{'open_tab': {'url': 'https://finance.yahoo.com/quote/TSLA/'}},
]

async def main():
    agent = Agent(
        task="What is Tesla(TSLA) latest stock price",
        llm=llm,
        initial_actions=initial_actions
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
