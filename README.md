# EXIT Token

`EXIT` is a privacy-focused ERC-20 token deployed on Ethereum (just for the start).

## ✅ Specs

- Name: EXIT
- Symbol: EXIT
- Decimals: 18
- Total Supply: 100,000,000 EXIT

## 🔐 Contract Security

- Written using OpenZeppelin audited libraries.
- `Ownable` contract used for mint control.

## 📄 Audit Report

See `/pdfs/ExitAudit-CertiK.pdf`

## 📜 Deployment

```bash
npx hardhat run scripts/deploy.js --network goerli
