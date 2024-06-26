from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from tgs.edges import AgentState, grade_documents
from tgs.nodes import agent, generate, rewrite
from tgs.tools import retriever_tool_questions, retriever_tool_summaries

workflow = StateGraph(AgentState)

workflow.add_node("agent", agent)
retrieve = ToolNode([retriever_tool_questions, retriever_tool_summaries])
workflow.add_node("retrieve", retrieve)
workflow.add_node("rewrite", rewrite)
workflow.add_node("generate", generate)
workflow.set_entry_point("agent")

workflow.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools": "retrieve",
        END: END,
    },
)

workflow.add_conditional_edges(
    "retrieve",
    grade_documents,
)
workflow.add_edge("generate", END)
workflow.add_edge("rewrite", "agent")

graph = workflow.compile()
