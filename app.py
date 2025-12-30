from fastapi import FastAPI
from startup import routes, loadModels


loadModels()

app = FastAPI()
routes(app)


