from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "WERO1WAGER" in response.text
    assert "VEGAS DIGITAL" in response.text
    assert "SEM APOSTAS REAIS" in response.text

def test_health():
    data = client.get("/health").json()
    assert data["status"] == "ready"
    assert data["real_money_betting"] is False
    assert data["payments_enabled"] is False
    assert data["transfers_enabled"] is False

def test_sports():
    response = client.get("/api/sports")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 24
    assert len(data["items"]) == 24

def test_events_are_synthetic():
    data = client.get("/api/events").json()
    assert data["source"] == "synthetic_demo"
    assert data["betting_enabled"] is False
    assert len(data["items"]) > 0

def test_financial_gate():
    data = client.get("/api/finance/summary").json()
    assert data["confirmed_revenue_brl"] == "0.00"
    assert data["transfers_enabled"] is False
    assert data["verified_provider"] is False

def test_unknown_route():
    assert client.get("/api/bet").status_code == 404
