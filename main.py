from fastapi import FastAPI
from deta import Deta
from routers import crawler, auth

app = FastAPI()
deta = Deta("a09qh2ra_LhduPUAxEAXiC4KDSXkq1teE3P5VA1xi")

# Including Routers from .routers
app.include_router(crawler.router)
app.include_router(auth.router)


@app.get("/")
def app_index():
    return ["/crawler", "/user"]
