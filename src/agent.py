from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import langgraph.graph as graph

def run_agent():
    # Create the agent
    memory = MemorySaver()
    model = ChatOpenAI(model_name="gpt-4")  # Changed to OpenAI's GPT-4
    tools = []  # Initialize with empty tools collection
    agent_executor = create_react_agent(model, tools, checkpointer=memory)

    # Export the graph as PNG
    graph.export_graph(agent_executor, "agent_graph.png")

    # Use the agent
    config = {"configurable": {"thread_id": "abc123"}}
    for step in agent_executor.stream(
        {"messages": [HumanMessage(content="hi im bob! and i live in sf")]},
        config,
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()

    for step in agent_executor.stream(
        {"messages": [HumanMessage(content="whats the weather where I live?")]},
        config,
        stream_mode="values",
    ):
        step["messages"][-1].pretty_print()