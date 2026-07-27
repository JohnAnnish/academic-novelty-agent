from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent

app = FastAPI(title="Academic Novelty Checker API")

# Allow the React frontend (running on a different port) to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NoveltyRequest(BaseModel):
    abstract: str

@app.post("/analyze")
async def analyze_abstract(request: NoveltyRequest):
    try:
        # Run our AI Agent using the abstract from the frontend
        report = run_agent(request.abstract)
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI Server on http://127.0.0.1:8000...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
