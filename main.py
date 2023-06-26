from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, PromptTemplate
from langchain.chat_models import PromptLayerChatOpenAI
from dotenv import load_dotenv

def create_prompt():
  human_message_prompt = HumanMessagePromptTemplate(
      prompt=PromptTemplate(
        template="My name is {name}",
        input_variables=["name"],
      )
    )
  return ChatPromptTemplate.from_messages([human_message_prompt])


def main():
  chat_prompt = create_prompt()
  messages = chat_prompt.format_prompt(name="YOUR_NAME").to_messages()

  model = PromptLayerChatOpenAI(model_name="gpt-3.5-turbo", pl_tags=["docs-discussion"])
  output = model(messages)
  print(output)

if __name__ == "__main__":
    load_dotenv()
    main()