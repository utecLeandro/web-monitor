from fastapi import FastAPI, Query
import httpx, time

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics/web")
def web_metrics(url: str = Query("https://www.mercadolibre.com.uy/")):
    t0 = time.perf_counter()
    try:
        r = httpx.get(url, timeout=5.0)
        elapsed_ms = (time.perf_counter() - t0) * 1000
        return {"url": url, "status_code": r.status_code, "response_time_ms": elapsed_ms}
    except Exception as e:
        elapsed_ms = (time.perf_counter() - t0) * 1000
        return {"url": url, "error": str(e), "response_time_ms": elapsed_ms}
