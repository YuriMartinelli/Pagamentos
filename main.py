from fastapi import FastAPI

from app.routes.usuarios_routes import usuarios_router

app = FastAPI()


@app.get("/ping")
def pong() -> dict[str, str]:
    return {"ping": "pong!"}


app.include_router(usuarios_router)
