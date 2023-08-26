import os
from fastapi import FastAPI, Request, Response, status as STATUS
from fastapi.middleware.cors import CORSMiddleware
from httpcore import Origin
from pydantic import BaseModel
from typing import Optional, List
from schemas import AnswerBaseSchema
from database import SessionLocal
import models
from routes import router  # Import the router


app = FastAPI(
    title="fastapi-sec-store",         # Add your app's title here
    description="Headshed FastAPI secure store takes posted json data and stores, then retrieves data for logged in and authorised users"  # Add your app's description here
)    
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

# Custom middleware to block access to /docs and /redoc
@app.middleware("http")
async def block_docs_and_redoc(request: Request, call_next):
    disable_docs = os.environ.get("DISABLE_DOCS", "false").lower() == "true"
    
    if disable_docs and (request.url.path.startswith("/docs") or request.url.path.startswith("/redoc")):
        response = Response(content="Access to documentation is restricted.", status_code=403)
        return response
    return await call_next(request)

db = SessionLocal()

# Mount the imported router with prefix on the app instance
app.include_router(router)