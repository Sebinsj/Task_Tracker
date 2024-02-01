from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from database import(
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    delete_todo,
)


#App Object

app=FastAPI()

origins=['https://localhost:3000']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {"ping":"pong"}


@app.get('/api/todo')
async def get_todo():
    response=await fetch_all_todos()
    return response


@app.get('/api/todo{title}',response_model=Todo)
async def get_todo_by_id(title):
    response=await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404,f"there is no todo item with this title{title}")




@app.post('/api/todo',response_model=Todo)
async def post_todo(todo:Todo):
    
    return 1





@app.put('/api/todo{id}')
async def put_todo(id,data):
    return 1




@app.delete('/api/todo{id}')
async def delete_todo(id):
    return 1
