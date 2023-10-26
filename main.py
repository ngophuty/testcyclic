from fastapi import FastAPI, Depends

app = FastAPI()


@app.get('/')
async def hello():
    return "hello"