# Wero1Wager — partner finance sandbox
Date: 2026-10-22. Development proposal only; production remains unchanged.

The ledger models partner onboarding and CPA/revenue-share commissions in memory. It never registers users, redirects to gambling operators, publishes campaigns, handles deposits, executes payouts or connects to a bank. Example partners are fictional. No real partner authorization or banking evidence has been verified.

## Mandatory gates before any real integration
- Independently validate the operator licence for the exact target country, permitted products and advertising channels.
- Obtain a written affiliate agreement, local legal review, and any affiliate licence/registration.
- Confirm the contracting entity's eligibility, KYC, tax treatment, settlement currency, fees, payout schedule and destination bank ownership.
- Add geo-restrictions, age controls, consent, responsible gambling rules and audit logging before any permitted advertising.
- Verify source-of-truth provider statements and bank evidence before marking a transfer confirmed.
- Keep simulated balances segregated from verified balances. Never fabricate clicks, deposits, revenue or receipts.
- Test in isolated staging and obtain explicit release approval. No automatic promotion to main.

Run offline tests: `python -m unittest discover -s tests -v`.
