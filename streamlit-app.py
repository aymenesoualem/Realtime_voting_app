import time

import psycopg2
import streamlit as st


st.write("Realtime Election Voting Dashboard")
@st.cache_data
def fetch_voting_stats():
    conn = psycopg2.connect("host=localhost dbname=voting user=postgres password=postgres")
    cur = conn.cursor()
    cur.execute("""
    SELECT count(*) voters_count from voters
    """)

    voters_count = cur.fetchone()[0]

    cur.execute("""
    SELECT count(*) candidates_count from candidates""")

    candidates_count = cur.fetchone()[0]
    return voters_count, candidates_count

def update_data():
    last_refresh = st.empty
    last_refresh.text(f"Last Refreshed: {time.strftime('%Y/%m/%d %H:%M:%S')}")

    voters_count, candidates_count = fetch_voting_stats()

    st.markdown("""___""")

    col1, col2 = st.columns(2)

    col1.metric("Total Voters", value=voters_count)
    col1.metric("Total Candidates", value=candidates_count)
