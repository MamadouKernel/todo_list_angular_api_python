from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.tasks_router import router as tasks_router

app = FastAPI()
# Ajouter la middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # mettre à jour pour les domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)
