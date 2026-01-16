from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/punish")
def trigger_punishment():
    print("Punishment Triggered: Reverting Git...")
    result = subprocess.run(
        ["git", "reset", "--hard", "HEAD~1"], 
        cwd="..", 
        capture_output=True, 
        text=True
    )
    if result.returncode == 0:
        return {"status": "success", "message": "Git reset successful."}
    else:
        return {"status": "error", "message": result.stderr}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)