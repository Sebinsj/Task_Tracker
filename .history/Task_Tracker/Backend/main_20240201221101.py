from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async de