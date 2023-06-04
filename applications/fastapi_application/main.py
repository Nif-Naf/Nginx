from fastapi import FastAPI

first_app = FastAPI()


@first_app.get("/")
def read_hood():
    return {"HELLO": "World"}


@first_app.get("hello")
def read_root():
    return {"Hello": "World"}
