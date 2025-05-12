from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

root = APIRouter()

templates = Jinja2Templates(directory="src/app/templates")

@root.get("/", response_class=HTMLResponse)
async def template_root(request: Request):
    return templates.TemplateResponse("layouts/root.jinja2", { "request": request })