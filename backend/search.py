from urllib import response
from jina import Client
from docarray import Document
from config import HOST
import streamlit as st
DATABASE_FILE = "/home/aswin/Documents/example-knowledge-base-stackoverflow/data/small/answers.sqlite"
def search_by_text(input, server=HOST):
    client = Client(host=server)
    response = client.search(
        Document(text=input),
        # parameters={"limit": limit},
        return_results=True,
    )
    return response
def get_answers(question_id, db_file=DATABASE_FILE, table_name="Answers", id_field="ParentId"):
    import sqlite3 as db

    conn = db.connect(db_file)
    sql = f"SELECT * FROM {table_name} WHERE {id_field} = {question_id}"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    answers = []

    for row in rows:
        answer = {
            "Body": row[6],
            "Score": row[4],
            "IsAcceptedAnswer": row[5]
        }
        answers.append(answer)

    return answers
def html_to_markdown(html, code_language="r"):
    from markdownify import markdownify
    markdown = markdownify(html, heading_style="ATX", code_language=code_language)

    return markdown
user_input = st.text_input("Enter your query", key="input")
search_button = st.button("Search")
if search_button:
    result =search_by_text(user_input)

    matches = result[0].matches
    for match in matches:
        st.markdown(html_to_markdown(match.text))
        # print(match.id)
        # answers = get_answers(question_id=match.id)
        # for answer in answers:
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        #     st.markdown(html_to_markdown(answer["Score"]))
        #     st.markdown(html_to_markdown(answer["IsAcceptedAnswer"]))
        #     st.markdown(html_to_markdown(answer["Body"]))
        # st.markdown(f"{match.text}")
        # st.markdown(match.tags)
        # st.markdown("---")
        # st.markdown(html_to_markdown(match.tags["Body"]))
        # st.markdown("Answers")
        # print(match.text)
        # print(match.tags)
        # print("---")