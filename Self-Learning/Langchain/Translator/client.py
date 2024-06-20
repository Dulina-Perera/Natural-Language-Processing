from langserve import RemoteRunnable

remote_chain: RemoteRunnable = RemoteRunnable("http://localhost:8000/chain")

response: str = remote_chain.invoke({
    "language": "Italian",
    "text": "Hello, World!"
})
print(response)
