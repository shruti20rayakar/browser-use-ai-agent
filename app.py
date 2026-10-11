
import asyncio
import streamlit as st
from dotenv import load_dotenv
from browser_use import Agent, ChatGoogle

load_dotenv()

st.title("AI Browser Agent")
st.write("Give your AI agent a task to perform.")

task = st.text_input(
    "Enter your task",
    value="Open https://example.com and tell me its page title."
)

if st.button("Run Agent"):
    if task.strip():
        with st.spinner("Agent is working..."):
            try:
                async def run_agent():
                    agent = Agent(
                        task=task,
                        llm=ChatGoogle(model="gemini-3.8-flash"),
                    )
                    result = await agent.run()
                    return result.final_result()

                result = asyncio.run(run_agent())
                st.write("Result:", result or "No result returned.")

            except Exception as e:
                st.error(f"Error: {e}")
