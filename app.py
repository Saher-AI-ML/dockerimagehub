from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/",response_class=HTMLResponse)

def welcome_message():
    return "Hello there"
