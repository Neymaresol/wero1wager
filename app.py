from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from provider_registry import provider_status

app = FastAPI(title="Wero1Wager PARADIGMA", version="0.3.1-rc")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
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
@app.get("/api/providers/status")
def providers_status():
    return provider_status()

@app.get("/api/finance/summary")
def finance():
    return {"confirmed_revenue_brl":"0.00","simulated_revenue_brl":"0.00","transfers_enabled":False,"verified_provider":False}
@app.get("/",response_class=HTMLResponse)
def index():
    return Path(__file__).with_name("index.html").read_text(encoding="utf-8")
