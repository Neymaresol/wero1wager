"""Offline-only partner commission ledger. No payment or betting integration."""
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from enum import Enum

class State(str, Enum):
    SIMULATED = "simulated"
    ACCRUED = "accrued"
    APPROVED = "approved"
    WITHDRAWABLE = "withdrawable"
    TRANSFERRED = "transferred"

@dataclass(frozen=True)
class Partner:
    name: str
    jurisdiction: str
    currency: str
    contract_verified: bool = False
    marketing_approved: bool = False

@dataclass(frozen=True)
class LedgerEntry:
    partner: Partner
    amount: Decimal
    state: State = State.SIMULATED
    evidence_reference: str = ""
    simulation: bool = True

    def __post_init__(self):
        if not self.amount.is_finite() or self.amount < 0:
            raise ValueError("Amount must be finite and non-negative")
        if not self.simulation and self.state == State.TRANSFERRED and not self.evidence_reference:
            raise ValueError("Confirmed transfers require provider/bank evidence")

def simulate_cpa(qualified_customers: int, fee: str, partner: Partner) -> LedgerEntry:
    if not isinstance(qualified_customers, int) or isinstance(qualified_customers, bool) or qualified_customers < 0:
        raise ValueError("Qualified customers must be a non-negative integer")
    try:
        amount = Decimal(fee) * qualified_customers
    except (InvalidOperation, TypeError):
        raise ValueError("Invalid CPA fee") from None
    return LedgerEntry(partner=partner, amount=amount)

def simulate_revenue_share(net_revenue: str, percentage: str, partner: Partner) -> LedgerEntry:
    try:
        revenue, rate = Decimal(net_revenue), Decimal(percentage)
    except (InvalidOperation, TypeError):
        raise ValueError("Invalid amount or rate") from None
    if not revenue.is_finite() or revenue < 0 or not rate.is_finite() or not (0 <= rate <= 100):
        raise ValueError("Revenue must be non-negative and percentage between 0 and 100")
    return LedgerEntry(partner=partner, amount=revenue * rate / 100)

def public_summary(entries: list[LedgerEntry]) -> dict:
    """Only provider/bank-evidenced real transfers may count as confirmed."""
    confirmed = sum((e.amount for e in entries if not e.simulation and e.state == State.TRANSFERRED and e.evidence_reference), Decimal("0"))
    simulated = sum((e.amount for e in entries if e.simulation), Decimal("0"))
    return {"confirmed_transfers": str(confirmed), "simulated_commissions": str(simulated), "live_payments_enabled": False, "advertising_enabled": False}
