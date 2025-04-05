from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def ping():
    return {"message": "pong"}


@router.get("/add:n")
def add(n: int):
    return {"result": n + 1}
