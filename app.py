from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr

load_dotenv(override=True)

MODEL_NAME = "qwen3:0.6b"

openai = OpenAI()

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        type="messages",
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False, type="messages"),
        css=CSS,
        theme=gr.themes.Base(),
    ).launch()