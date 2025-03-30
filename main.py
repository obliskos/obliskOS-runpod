from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Make sure you're using the correct new OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Søren Vale. Write in a bold, strategic, and philosophical voice."},
            {"role": "user", "content": request.prompt}
        ]
    )
    return {"response": response.choices[0].message.content}
