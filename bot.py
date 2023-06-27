from langchain import PromptTemplate, LLMChain
from langchain.llms import PromptLayerOpenAI
import chainlit as cl
from dotenv import load_dotenv
load_dotenv()

@cl.on_chat_start
async def main():
    res = await cl.AskUserMessage(content="Hi, I'm here to help you learn. Enter the URL for the documentation or describe what you need and I'll find some relavent docs.",
                                   timeout=10).send()
    if res:
        await cl.Message(
            content=f"Looking into {res['content']} now...",
        ).send()
