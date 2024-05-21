from fastapi import FastAPI
from .routes import hotpepper

app = FastAPI()

app.include_router(hotpepper.router)