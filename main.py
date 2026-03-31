
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Anu"}]

@app.post("/users")
def create_user():
    return {"id": 2, "name": "New User"}
