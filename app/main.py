from fastapi import FastAPI
from app.routes.ping import router as ping_router

app = FastAPI()

# Include the ping route
app.include_router(ping_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
