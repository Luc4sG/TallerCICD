from fastapi import FastAPI

test = 'test'

app = FastAPI()
@app.get("/")

async def root():
    return {"message": "Hola Mundo"}
