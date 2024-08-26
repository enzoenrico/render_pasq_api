import json
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/process')
async def process_file():
    with open('foo-page-1-table-1.json') as f:
        data = f.read()
    return json.loads(data)
