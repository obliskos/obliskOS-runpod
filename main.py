from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": request.prompt}
        ]
    )
    return {"response": response.choices[0].message["content"]}
