from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import analytics

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analytics.router)

@app.get("/")
def read_root():
    return {"status": "ok", "service": "Agency Dash Analytics"}
