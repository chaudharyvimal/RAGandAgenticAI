from langchain_ollama import OllamaLLM
import gradio as gr

llm = OllamaLLM(model="phi3:mini", base_url="http://127.0.0.1:11434")
# print(llm.invoke("Hi"))

# Get the query from the user input
# query = input("Please enter your query: ")
# response = llm.invoke(query)
# print(response.content)  # .content holds the model's text
# print(response)  # .content holds the model's text

# Function to generate a response from the model
def generate_response(prompt_txt):
    generated_response = llm.invoke(prompt_txt)
    return generated_response

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    # allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Chatbot",
    description="Ask any question and the chatbot will try to answer."
)
# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port= 7860)