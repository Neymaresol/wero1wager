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


def test_provider_status_never_claims_live_connection():
    data = client.get("/api/providers/status").json()
    assert data["real_money_betting"] is False
    assert len(data["providers"]) == 4
    assert all(p["connected"] is False for p in data["providers"])
    assert all(p["latency_ms"] is None for p in data["providers"])
    assert all(p["referrals_enabled"] is False for p in data["providers"])


def test_multilingual_bundle_is_served():
    response = client.get("/static/i18n.js")
    assert response.status_code == 200
    assert "localStorage" in response.text
    assert "pt-BR" in response.text
    assert "translations" in response.text


def test_multilingual_selector_in_html():
    html = client.get("/").text
    assert 'id="language"' in html
    assert '/static/i18n.js' in html
    assert 'value="en"' in html
    assert 'value="es"' in html


def test_no_unverified_live_market_claims():
    response = client.get("/api/providers/status")
    assert response.status_code == 200
    data = response.json()
    assert all(not p["connected"] for p in data["providers"])
    assert all(p["data_freshness"] == "unavailable" for p in data["providers"])


def test_premium_assets_gate():
    """A Vegas Digital release requires every approved visual asset."""
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    required = ["logo.webp", "werozinha.webp", "sports.webp", "casino.webp", "virtual.webp", "esports.webp", "ai.webp", "bonus.webp", "referencia-original.webp"]
    missing = [name for name in required if not (root / "static" / "assets" / name).is_file()]
    assert not missing, f"Premium Vegas Digital release blocked: missing assets: {missing}"
