from fastapi import FastAPI
from routers import crawler, auth

app = FastAPI()


@app.get("/")
def app_index():
    return ["/crawler", "/users/me"]


@app.get("/users")
def users():
    return "/me"


app.include_router(crawler.router)
app.include_router(auth.router)
