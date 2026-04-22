from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -------------------------
# 📦 Pydantic Models
# -------------------------

class User(BaseModel):
    id: int
    name: str

class UserCreate(BaseModel):
    name: str

class UserUpdate(BaseModel):
    name: str


# -------------------------
# 🗂️ In-memory DB
# -------------------------

users_db: List[User] = [
    User(id=1, name="Anu"),
    User(id=2, name="New User")
]


# -------------------------
# 🌐 Routes
# -------------------------

@app.get("/")
def read_root():
    return {"message": "Hello World"}


# GET all users
@app.get("/users", response_model=List[User])
def get_users():
    return users_db


# POST create user (PROPER BODY)
@app.post("/users", response_model=User)
def create_user(user: UserCreate):
    new_user = User(
        id=len(users_db) + 1,
        name=user.name
    )
    users_db.append(new_user)
    return new_user


# GET user by ID
@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# PUT update user (BODY instead of query)
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_data: UserUpdate):
    for user in users_db:
        if user.id == user_id:
            user.name = updated_data.name
            return user
    raise HTTPException(status_code=404, detail="User not found")


# DELETE user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


# SEARCH users
@app.get("/search", response_model=List[User])
def search_users(name: str = Query(...)):
    return [
        user for user in users_db
        if name.lower() in user.name.lower()
    ]



        reverse=(order == "desc")
    )
    return sorted_users
