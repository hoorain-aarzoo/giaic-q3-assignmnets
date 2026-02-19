from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Todo List API")

# -------------------------
# Pydantic Model
# -------------------------
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# -------------------------
# Fake Database
# -------------------------
todos: List[Todo] = []

# -------------------------
# ROOT ROUTE
# -------------------------
@app.get("/")
def home():
    return {"message": "Todo API is running"}

# -------------------------
# CREATE Todo
# -------------------------
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo created successfully",
        "todo": todo
    }

# -------------------------
# READ All Todos
# -------------------------
@app.get("/todos")
def get_all_todos():
    return todos

# -------------------------
# READ Single Todo
# -------------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

# -------------------------
# UPDATE Todo
# -------------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "todo": updated_todo
            }
    return {"error": "Todo not found"}

# -------------------------
# DELETE Todo
# -------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    return {"error": "Todo not found"}
