from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import os 
from loguru import logger
from config import LOGDIR, LOGFILE, ORIGINS, BASEDIR

LOGDIR = BASEDIR + "/" + LOGDIR

if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)
    
logger.add(
    LOGDIR + "/" + LOGFILE,
    rotation="25MB",
    colorize=True,
    format="<green>{time:YYYYMMDD_HH:mm:ss}</green> | {level} | <level>{message}</level>",
    level="ERROR",
)

app= FastAPI()

origins = []

    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    
    
)
from api.views import main