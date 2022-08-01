from docarray import DocumentArray, Document
from jina import Flow, Client
from config import DATA_FILE, NUM_DOCS, HOST
import click

flow = Flow.load_config("flow-ann.yml")
q = Document(text="software")
with flow:
    flow.post(on="/search",HOST="0.0.0.0:52005", inputs=q)