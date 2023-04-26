import json
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from api.generator_creator import generate_website

load_dotenv('.env')

app = FastAPI()


@app.get("/")
def read_root(user_prompt):
    res = generate_website(user_prompt)    

    return {"template": res}
