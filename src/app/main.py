import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Example API",
    description="Kadaster API",
    version="0.0.1"
)


# Allow all origins, methods and headers
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Welcome to the root page!"}


@app.get("/welcome")
async def welcome():
    return {"message": "Welcome user to the API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5005)
