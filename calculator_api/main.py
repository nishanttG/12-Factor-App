from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from calculator_api.api.routes import router

app = FastAPI()
app.include_router(router, prefix="/api")

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    file_path = os.path.join("static", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
