from . import create_app
import uvicorn

app = create_app("Fake/Random Things", "1.0.0")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3030)
