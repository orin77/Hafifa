from fastapi import FastAPI
from src.routes import achievements_routes

app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(achievements_routes.router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
