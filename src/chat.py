from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

def run_chat():
    model = init_chat_model("gpt-4o-mini", model_provider="openai")

    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]

    result = model.invoke(messages)
    print(result.pretty_print())