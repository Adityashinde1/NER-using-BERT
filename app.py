import os
import sys
from fastapi import FastAPI, File
from uvicorn import run as app_run
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, JSONResponse
from train import training as start_training
#from ner.pipeline.prediction_pipeline import ModelPredictor
from ner.constant import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/train")
async def training():
    try:
        start_training()

        return Response("Training successful !!")

    except Exception as e:
        raise Response(f"Error Occurred! {e}")



if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)