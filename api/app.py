from fastapi import FastAPI, Request
from dotenv import load_dotenv
from api.generator_creator import generate_website, get_template
from api.redis_db import RedisDB

load_dotenv('.env')
RedisDB().start_db()

app = FastAPI()


@app.get("/")
def read_root(user_prompt):
    res = generate_website(user_prompt)    

    return {"template": res}


@app.get("/{_id}")
def read_root(_id):
    res = get_template(_id)

    return {"template": res}
