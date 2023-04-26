import json
from fastapi import FastAPI
from dotenv import load_dotenv
from api.generator_creator import generate_website

load_dotenv('.env')

app = FastAPI()


@app.get("/")
def read_root():
    res = generate_website('AI Workflow for startup and small business. We help with all ai tools integration.')

    return {"template": res}
