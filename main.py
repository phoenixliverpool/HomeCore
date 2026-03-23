from fastapi import FastAPI
import uvicorn

app = FastAPI(title="HomeCore")

# A simple welcome route
@app.get("/")
def read_root():
    return {"status": "HomeCore Online", "version": "0.1"}

# A fake light switch route
@app.get("/light/toggle")
def toggle_light():
    return {"action": "toggled", "device": "Living Room Light"}

# Run the server if this file is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)