from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from typing import List

import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

#Root
@app.get("/")
def root():
    return "ToDoList"

#Create
@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, session: Session = Depends(get_session)):
    
    # Create an instance of the ToDo database model
    tododb = models.ToDo(task = todo.task)
    
    # Add it to the session and commit it
    session.add(tododb)
    session.commit()
    session.refresh(tododb)
        
    # Insert todo as a new record in the database
    return tododb

#Read
@app.get("/todo/{id}", response_model = schemas.ToDo)
def read_todo(id: int, session: Session = Depends(get_session)):
    
    # Get the todo item with the given id
    todo = session.query(models.ToDo).get(id)
    
    # Checkin if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code = 404, detail = f"todo item with id {id} not found")
    
    return todo

    

#Update
@app.put("/todo/{id}")
def update_todo(id:int, task: str, session: Session = Depends(get_session)):
    
    # Get the todo item with given id
    todo = session.query(models.ToDo).get(id)
    
    # Upadate todo item with the given task (if an item with the given id was found)
    if todo:
        todo.task = task
        session.commit()
        
    
    # Check if todo item with the given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code = 404, detail = f"todo item with id {id} not found" )
    
    return todo

#Delete
@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, session: Session = Depends(get_session)):
    
    
    # Get the todo item with given id 
    todo = session.query(models.ToDo).get(id)
    
    # If todo item with given id exist, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
    else:
        raise HTTPException(status_code = 404, detail = f"todo item with id {id} not found") 
    
    return None

#Get All list
@app.get("/todo", response_model= List[schemas.ToDo])
def read_todo_list(session: Session = Depends(get_session)):
    
     # Get All Items
    todo_list = session.query(models.ToDo).all()

    
    return todo_list

'''
products = {
    1: {"name": "computer", "unit_price": 2000, "stock": 5},
    2: {"name": "iphone", "unit_price": 800, "stock": 10},
    3: {"name": "ps4 controller", "unit_price": 50, "stock": 4},
    4: {"name": "Brazil t-shirts", "unit_price": 300, "stock": 100}
}

#Simple first GET to create a route and show up a String
@app.get("/")
async def root():
    return {"message": "hello world this is Home"}

@app.get("/products")
def LenProducts():
    return {"How many types products Online": len(products)}

#Route to Id Products Error treatment 
@app.get("/products/{id_product}")
def getProduct(id_product: int):
    
    if id_product in products:
        return products[id_product]
    else:
        return {"Error": "ID doesnt exist"}
'''