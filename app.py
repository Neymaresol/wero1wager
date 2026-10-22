from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from datetime import datetime, timezone, timedelta
from threading import Lock
from uuid import UUID
from pydantic import BaseModel

app = FastAPI(title="Wero1Wager PARADIGMA", version="0.3.1-rc")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
# Prototype analytics store. One process only; reset on restart.
_presence_lock = Lock()
_active_sessions = {}
_online_window = timedelta(seconds=60)

class Heartbeat(BaseModel):
    session_id: UUID

@app.post("/api/audience/heartbeat")
def audience_heartbeat(payload: Heartbeat):
    now = datetime.now(timezone.utc)
    with _presence_lock:
        cutoff = now - _online_window
        expired = [key for key, seen in _active_sessions.items() if seen < cutoff]
        for key in expired:
            del _active_sessions[key]
        _active_sessions[str(payload.session_id)] = now
    return {"accepted": True, "ttl_seconds": 60}

@app.get("/api/audience/online")
def audience_online():
    now = datetime.now(timezone.utc)
    with _presence_lock:
        cutoff = now - _online_window
        expired = [key for key, seen in _active_sessions.items() if seen < cutoff]
        for key in expired:
            del _active_sessions[key]
        count = len(_active_sessions)
    return {"online_sessions": count, "window_seconds": 60, "source": "ephemeral_single_process", "scope": "current_instance", "measured_at": now.isoformat()}

SPORTS = ["Futebol","Basquete","Tênis","Vôlei","Futebol americano","Beisebol","Hóquei","Automobilismo","MMA","Boxe","eSports","Rúgbi","Handebol","Críquete","Ciclismo","Golfe","Tênis de mesa","Badminton","Natação","Atletismo","Esportes de inverno","Surfe","Skate","Xadrez"]
EVENTS = [{"sport":"Futebol","name":"Aurora × Eclipse"},{"sport":"Basquete","name":"Titãs × Cometas"},{"sport":"Tênis","name":"Jogador A × Jogador B"},{"sport":"eSports","name":"Nexus × Vortex"}]
@app.get("/health")
def health():
    return {"service":"wero1wager","version":"0.3.1-rc","status":"ready","data_source":"demo","real_money_betting":False,"payments_enabled":False,"transfers_enabled":False}
@app.get("/api/sports")
def sports():
    return {"items":SPORTS,"count":len(SPORTS),"source":"static"}
@app.get("/api/events")
def events():
    return {"items":EVENTS,"source":"synthetic_demo","betting_enabled":False}
@app.get("/api/finance/summary")
def finance():
    return {"confirmed_revenue_brl":"0.00","simulated_revenue_brl":"0.00","transfers_enabled":False,"verified_provider":False}
@app.get("/",response_class=HTMLResponse)
def index():
    return Path(__file__).with_name("index.html").read_text(encoding="utf-8")
