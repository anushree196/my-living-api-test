
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dummy in-memory data
users_db = [
    {"id": 1, "name": "Anu"},
    {"id": 2, "name": "New User"}
]

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return users_db

@app.post("/users")
def create_user():
    new_user = {"id": len(users_db) + 1, "name": "New User"}
    users_db.append(new_user)
    return new_user

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str):
    for user in users_db:
        if user["id"] == user_id:
            user["name"] = name
            return {"message": "User updated", "user": user}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}
