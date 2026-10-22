import unittest
from decimal import Decimal
from partner_ledger import Partner, LedgerEntry, State, simulate_cpa, simulate_revenue_share, public_summary

class PartnerLedgerTests(unittest.TestCase):
    def setUp(self):
        self.partner = Partner("Example only", "GB", "GBP")

    def test_cpa_is_simulated(self):
        entry = simulate_cpa(10, "25", self.partner)
        self.assertEqual(entry.amount, Decimal("250"))
        self.assertEqual(public_summary([entry])["confirmed_transfers"], "0")

    def test_revenue_share(self):
        self.assertEqual(simulate_revenue_share("1000", "15", self.partner).amount, Decimal("150"))

    def test_reject_invalid_inputs(self):
        for fee in ("-1", "NaN", "Infinity"):
            with self.assertRaises(ValueError):
                simulate_cpa(1, fee, self.partner)
        with self.assertRaises(ValueError):
            simulate_revenue_share("100", "101", self.partner)

    def test_transfer_requires_evidence(self):
        with self.assertRaises(ValueError):
            LedgerEntry(self.partner, Decimal("100"), State.TRANSFERRED, simulation=False)

    def test_real_evidenced_transfer(self):
        entry = LedgerEntry(self.partner, Decimal("100"), State.TRANSFERRED, "bank-reference", False)
        self.assertEqual(public_summary([entry])["confirmed_transfers"], "100")

if __name__ == "__main__":
    unittest.main()
