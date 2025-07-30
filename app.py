import gradio as gr
from chatbot.qa_chain import setup_chain, ask_bot

# Setup once when the app starts
db = setup_chain()

def chatbot_interface(user_input, history):
    response = ask_bot(db, user_input)
    history.append((user_input, response))
    return history, history

# Launch the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("### 🤖 OrbitApp Support Bot")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask your question here")
    clear = gr.Button("Clear")

    state = gr.State([])

    msg.submit(chatbot_interface, [msg, state], [chatbot, state])
    clear.click(lambda: ([], []), None, [chatbot, state])

demo.launch()
