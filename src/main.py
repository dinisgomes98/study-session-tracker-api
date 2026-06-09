from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"status": "study session tracker api is running"}