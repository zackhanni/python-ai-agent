from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini")
response = llm.invoke("What is the meaning of life?")
# llm = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
print(response)