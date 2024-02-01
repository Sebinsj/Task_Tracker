from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware

#App Object

app=FastAPI()

origins=['https://localhost:300']