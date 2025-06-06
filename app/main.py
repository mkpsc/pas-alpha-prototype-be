from fastapi import FastAPI
from app.patients.router import router as patients_router
import uvicorn


app = FastAPI()

app.include_router(patients_router, prefix="/patients")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
