import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import PromptLayerOpenAI
import chainlit as cl
from dotenv import load_dotenv
load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=PromptLayerOpenAI(temperature=0, pl_tags=["docs-discussion"]), verbose=True)

    return llm_chain
