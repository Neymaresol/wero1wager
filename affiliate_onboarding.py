"""Compliance-first affiliate onboarding; no outbound tracking or gambling actions."""
from dataclasses import dataclass
from urllib.parse import urlsplit

@dataclass(frozen=True)
class AffiliateApplication:
    operator: str
    country: str
    license_verified: bool = False
    affiliate_contract_signed: bool = False
    marketing_approved: bool = False
    age_geo_controls_reviewed: bool = False
    destination_url: str = ""
    affiliate_attribution_verified: bool = False

def evaluate_application(a: AffiliateApplication) -> dict:
    """Fail closed until independently evidenced authorizations exist."""
    try:
        u = urlsplit(a.destination_url)
        destination_valid = (u.scheme == "https" and bool(u.hostname)
                             and not u.username and not u.password
                             and u.port in (None, 443) and not u.fragment)
    except (ValueError, TypeError):
        destination_valid = False
    checks = {
        "operator_identified": bool(a.operator.strip()),
        "jurisdiction_identified": bool(a.country.strip()),
        "license_verified": a.license_verified is True,
        "contract_signed": a.affiliate_contract_signed is True,
        "marketing_approved": a.marketing_approved is True,
        "age_geo_controls_reviewed": a.age_geo_controls_reviewed is True,
        "destination_valid": destination_valid,
        "attribution_verified": a.affiliate_attribution_verified is True,
    }
    return {"approved": all(checks.values()), "checks": checks,
            "referrals_enabled": False, "payments_enabled": False,
            "note": "Assessment only. No production integration or marketing activation."}
