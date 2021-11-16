from fastapi import FastAPI

roomate_api = FastAPI()


@roomate_api.get("/")
async def root():
    return {"message": "Hello World"}
