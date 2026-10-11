
import asyncio
from dotenv import load_dotenv
from browser_use import Agent, ChatGoogle

load_dotenv()

async def main():
    agent = Agent(
        task="Open https://example.com and report its page title and main heading in one sentence.",
        llm=ChatGoogle(model="gemini-3.8-flash"),
    )

    result = await agent.run()
    print("Agent result:", result.final_result())

if __name__ == "__main__":
    asyncio.run(main())
