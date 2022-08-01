from docarray import DocumentArray
from jina import Flow
flow = Flow.load_config("flow-ann.yml")
docs = DocumentArray.from_csv(
        "/home/aswin/Documents/example-knowledge-base-search/backend/data/community.csv", field_resolver={"question": "text"}, size=30)
with flow:
        flow.index(docs, show_progress=True)