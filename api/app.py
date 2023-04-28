from fastapi import FastAPI, Request, Body
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

from api.generator_creator import generate_website, get_template
from api.redis_db import RedisDB

load_dotenv('.env')
RedisDB().start_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-web-generator-frontend.vercel.app/", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/")
def read_root(payload: dict = Body(...)):
    user_prompt = payload['user_prompt']
    _id, template = generate_website(user_prompt)

    return {"_id": _id, "template": template}


@app.get("/{_id}")
def read_root(_id):
    res = get_template(_id)

    return {"template": res}
