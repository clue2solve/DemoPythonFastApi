from fastapi import FastAPI

app = FastAPI()

@app.get('/api/v1/health')
def get():
    return "OK"

@app.get('/api/v1/health/version')
def getVersion():
    return '1.0.0'