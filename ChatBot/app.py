# %%
import streamlit as st

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from typing import List

load_dotenv()

# %%
def get_response(query: str, chat_history: List[AIMessage | HumanMessage]) -> str:
    template: str = """
        You are a helpful assistant.
        Answer the following questions considering the history of the conversation:

        Chat history: {chat_history}

        User question: {query}
    """

    prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(template)
    
    llm: ChatOpenAI = ChatOpenAI()

    chain = prompt | llm | StrOutputParser()
    return chain.stream({
        "query": query,
        "chat_history": chat_history
    })

# %%
st.set_page_config(page_title="Streaming Bot", page_icon="🤖")

st.title("Streaming Bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history: List[AIMessage | HumanMessage] = list() # type: ignore

# Conversation history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)

# User input
user_query: str | None = st.chat_input("Your message")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response: str = st.write_stream(get_response(user_query, st.session_state.chat_history))

    st.session_state.chat_history.append(AIMessage(ai_response))
