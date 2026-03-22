import gradio as gr

def create_ui(pipeline):

    def ask_fn(query):
        return pipeline.run("gradio_user", query)

    def summarize_fn():
        return pipeline.summarize("gradio_user")

    with gr.Blocks() as demo:
        gr.Markdown("# 🤖 GenAI RAG Bot")

        query = gr.Textbox(label="Ask your question")
        output = gr.Textbox(label="Response")

        ask_btn = gr.Button("Ask")
        ask_btn.click(ask_fn, inputs=query, outputs=output)

        summary_btn = gr.Button("Summarize")
        summary_btn.click(summarize_fn, outputs=output)

    return demo