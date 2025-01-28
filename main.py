from fastapi import FastAPI

from app.routes.usuarios_routes import USUARIOS_ROUTER

app = FastAPI()


@app.get("/ping")
def pong() -> dict[str, str]:
    return {"ping": "pong!"}


app.include_router(USUARIOS_ROUTER)
