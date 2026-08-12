import streamlit as st
from ollama import chat
from tools import calculator

st.set_page_config(
    page_title="Offline AI Agent",
    page_icon="🤖"
)

st.title("🤖 Offline AI Agent")
st.write("Local LLM + Tool Calling")

user_input = st.chat_input("Ask your question...")

if user_input:

    st.chat_message("user").write(user_input)

    tools = [calculator]

    messages = [
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = chat(
        model="llama3.2:1b",
        messages=messages,
        tools=tools
    )

    if response.message.tool_calls:

        call = response.message.tool_calls[0]

        args = call.function.arguments

        result = calculator(
            float(args["a"]),
            float(args["b"]),
            args["operation"]
        )

        messages.append(response.message)

        messages.append({
            "role": "tool",
            "content": str(result)
        })

        final = chat(
            model="llama3.2:1b",
            messages=messages,
            tools=tools
        )

        answer = final.message.content

    else:
        answer = response.message.content

    st.chat_message("assistant").write(answer)