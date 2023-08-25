from fastapi import FastAPI, status as STATUS, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from httpcore import Origin
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models 


app = FastAPI()
    
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/api/v1/healthchecker")
def health():
    return {"message": "Welcome to fastapi-sec-store  with Headshed"}    