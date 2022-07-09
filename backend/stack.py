from jina import Client
from docarray import Document
from config import HOST
def search_by_text(input, server=HOST):
    client = Client(host=server)
    response = client.search(
        Document(text=input),
        # parameters={"limit": limit},
        return_results=True,
    )
    return response
print(search_by_text("what is python class?"))