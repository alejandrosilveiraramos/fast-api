from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str
    
# complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str
    
    class Config:
        orm_mode = True
