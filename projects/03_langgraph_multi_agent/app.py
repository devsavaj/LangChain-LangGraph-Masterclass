import streamlit as st
from dotenv import load_dotenv
from langgraph.graph import StateGraph
from typing import TypedDict

from agents.researcher import researcher
from agents.analyst import analyst
from agents.writer import writer

load_dotenv()

st.title("🤖 LangGraph Multi-Agent System")

class AgentState(TypedDict):
    topic: str
    research: str
    analysis: str
    final_report: str

workflow = StateGraph(AgentState)

workflow.add_node("researcher", researcher)
workflow.add_node("analyst", analyst)
workflow.add_node("writer", writer)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "analyst")
workflow.add_edge("analyst", "writer")

app_graph = workflow.compile()

topic = st.text_input("Enter Topic")

if topic:
    result = app_graph.invoke({"topic": topic})
    st.write(result["final_report"])