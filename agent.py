from ollama import chat
from tools import calculator

tools = [calculator]

messages = [
    {
        "role": "user",
        "content": "What is 25 multiplied by 40?"
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
        args["a"],
        args["b"],
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

    print(final.message.content)

else:
    print(response.message.content)