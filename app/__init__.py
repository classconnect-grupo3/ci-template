from fastapi import FastAPI
from app.routes.ping import router as ping_router


def create_app() -> FastAPI:
    app = FastAPI()

    # Register routes
    app.include_router(ping_router)

    return app
