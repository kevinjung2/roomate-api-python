from fastapi import FastAPI

roomate_api = FastAPI()


@roomate_api.get("/")
async def root():
    return {"message": "Hello World"}

@roomate_api.get("/recipes")
async def recipies_index():
    return {"recipes": []}

@roomate_api.get("/recipes/{recipe_id}")
async def recipies_show(recipe_id: str):
    return {"recipes": recipe_id}

@roomate_api.get("/shopping_list")
async def shopping_list_index():
    return {"shopping_list": []}
