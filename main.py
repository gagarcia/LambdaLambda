from typing import Optional

from fastapi import FastAPI

from datetime import datetime

app = FastAPI()


@app.get("/hoje")
def read_root():
    today = datetime.today()

    return {
            "agora": today
        }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}