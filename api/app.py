from fastapi import FastAPI
from dotenv import load_dotenv
from api.generator_creator import generate_website
from api.redis_db import RedisDB

load_dotenv('.env')
RedisDB().start_db()

app = FastAPI()


@app.get("/")
def read_root():
    res = generate_website('AI Workflow for startup and small business. We help with all ai tools integration.')

    return {"template": res}
