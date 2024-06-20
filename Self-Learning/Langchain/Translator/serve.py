#!/usr/bin/env python
import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_mistralai import ChatMistralAI
from langserve import add_routes
from typing import List

# Load the environment variables.
load_dotenv()

# 1. Create the prompt template.
system_template: str = "Translate the following into {language}:"
prompt_template: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

# 2. Create the model.
model: ChatMistralAI = ChatMistralAI(
    model="mistral-small-latest", temperature=0, api_key=os.environ["MISTRAL_API_KEY"]
)

# 3. Create the parser.
parser: StrOutputParser = StrOutputParser()

# 4. Create the chain.
chain: RunnableSequence = prompt_template | model | parser


# 4. Define the FastAPI app.
app: FastAPI = FastAPI(
  title="LangChain Server",
  version="0.1",
  description="A simple API Server using LangChain's Runnable Sequences",
)

# 5. Add the routes.
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="localhost", 
        port=8000,
        log_level="info"
    )
