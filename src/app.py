from fastapi import FastAPI
from src.router import router

class App(FastAPI):
    def __init__(self):
        super().__init__()
        self.title = "Flow Carga"
        self.description = "Sistema de gerenciamento de transporte de cargas"
        self.version = "1.0.0"
        self.include_router(router)
        
