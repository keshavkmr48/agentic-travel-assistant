from fastapi import FastAPI

app = FastAPI(title='Agentic Travel Assistant')

@app.get('/health')
def health():
    return {'status':'ok'}
