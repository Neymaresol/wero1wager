"""Read-only provider registry. No real operators or odds feeds are connected."""
from datetime import datetime, timezone

PROVIDERS = (
    {"id": "demo-sports", "category": "sports", "display_name": "Sports demo feed"},
    {"id": "demo-esports", "category": "esports", "display_name": "eSports demo feed"},
    {"id": "demo-virtual", "category": "virtual", "display_name": "Virtual demo feed"},
    {"id": "demo-casino", "category": "casino", "display_name": "Casino demo feed"},
)

def provider_status():
    now = datetime.now(timezone.utc).isoformat()
    return {
        "source": "internal_configuration",
        "measured_at": now,
        "providers": [
            {**p, "mode": "demo", "connected": False, "licensed": False,
             "last_provider_update": None, "latency_ms": None,
             "data_freshness": "unavailable", "referrals_enabled": False}
            for p in PROVIDERS
        ],
        "real_money_betting": False,
    }
