from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Dockerized Python App!"}

@app.post("/generate_report")
def generate_report():
    # Simulated logic
    return {"status": "Report generated successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
