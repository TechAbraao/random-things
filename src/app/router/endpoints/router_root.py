from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

root = APIRouter()

templates = Jinja2Templates(directory="src/app/templates")

@root.get("/", response_class=HTMLResponse)
async def template_root(request: Request):
    data: List[str] = ["Random Name", "Random E-mail", "Random Address"]
    return templates.TemplateResponse("layouts/home.jinja2", {"request": request, "data": data})
