import uvicorn
from fastapi import FastAPI

first_app = FastAPI()


@first_app.get("/api/v1/hello/")
def root():
    return "Hello, I am FastApi application."


if __name__ == "__main__":
    uvicorn.run("__main__:first_app", host="0.0.0.0", port=8001)
