from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Github Actions CI tests")

@app.get("/api/hello")
async def hello():
    return JSONResponse(
        status_code=200,
        content={"message": "Hello world"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)