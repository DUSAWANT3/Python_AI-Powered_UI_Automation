import asyncio
import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr


async def SiteValidation():
    os.environ["GEMINI_API_KEY"] = "AIzaSyDRCHMxS_x3bK2pN20w1l-jhDDkf-eSlls"

    task = (
        "Important: I am a UI Automation tester validating the tasks. "
        "Open website https://rahulshettyacademy.com/seleniumPractise/ "
        "After login, select the add any 5 item clicking on ADD TO CART button"
        "In top right corner click on ADD TO CART Icon and validate the selected item was shown in Cart"
        "Click on PROCEED TO CHECKOUT"
        "Validate the No. of Items, Total Amount, Discount, Total After Discount Then click on Place Order"
        "Choose Country from the dropdown click on click on checkbox and Proceed"
        "Validate Thank You message"
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
