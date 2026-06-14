from fastapi import FastAPI
import os
import sys

app =FastAPI()


@app.get("/health")
def read_root():
    return{"status":"healthy"}

