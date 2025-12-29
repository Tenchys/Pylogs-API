from fastapi import FastAPI



app = FastAPI()


@app.get("/")
async def get():
    return '{"message": "hello world"}'

@app.get("/test")
async def test():
    return '{"message": "this is a test"}'