import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

#chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
