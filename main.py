import os
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from api.auth import auth
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
app.include_router(auth.router, prefix="/api/authentication", tags=["auth"])
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "default_secret_key"))

templates = Jinja2Templates(directory="static/")

@app.get("/")
async def login(request: Request):
    """
    :param request: An instance of the `Request` class, representing the incoming HTTP request.
    :return: A TemplateResponse object rendering the "login.html" template with the given request context.
    """
    return templates.TemplateResponse("pages/login/login.html", {"request": request})

@app.get("/welcome")
async def welcome(request: Request):
    """
    :param request: The incoming HTTP request containing session data.
    :return: A TemplateResponse object that renders the welcome page with the user's name or 'Guest' if not found.
    """
    name = request.session.get('user_name', 'Guest')
    context = {"request": request, "name": name}
    return templates.TemplateResponse("pages/welcome/welcome.html", context)

