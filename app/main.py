from fastapi import FastAPI
import os,sys

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

