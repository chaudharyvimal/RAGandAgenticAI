

# pip install langchain
# pip install google-genai-langchain

import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = "AIzaSyAifR5_keYmzHqSwM6GV0OO27hHzK-0UyM"
# "AIzaSyDqgOTIOfs84B0l9Nx49XSL9wvg8sGLh04"
# "AIzaSyAifR5_keYmzHqSwM6GV0OO27hHzK-0UyM" 
# "AIzaSyBGrL0f-aVtHEtd_eNs-zqOLXdZQaa1E2A"
model = init_chat_model("google_genai:gemini-2.5-flash-lite", temperature = 0.0,max_output_tokens = 50)

text = """
Only reply with the answer. What is the capital of Canada?
"""

print(model.invoke(text).content)


