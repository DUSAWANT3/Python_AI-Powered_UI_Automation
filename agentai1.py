import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr


async def SiteValidation():
    os.environ["GEMINI_API_KEY"] = "AIzaSyDRCHMxS_x3bK2pN20w1l-jhDDkf-eSlls"

    task = (
        "Important: I am a UI Automation tester validating the tasks. "
        "Open website https://rahulshettyacademy.com/loginpagePractise/ "
        "Login with username and password. Login details available in the system. "
        "After login, select the first 2 products and add them to the cart. "
        "Then checkout and store the total value you see on the screen. "
        "Increase the quantity of any product and check if the total value updates accordingly. "
        "select country, click on checkbox, and purchase."
    )

    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))

    agent = Agent(task, llm, use_vision=True)

    # This is inside the async function, so it's correct
    history = await agent.run()
    test_result = history.final_result()
    print(test_result)


# Ensure the async function is called properly
asyncio.run(SiteValidation())
