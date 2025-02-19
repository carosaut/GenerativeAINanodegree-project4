from fastapi import FastAPI
from api import router

### create app ###

app = FastAPI()

### import routes ###

app.include_router(router)




