# 🚫 My DNS Blocklist (Auto-Updated)

A personal DNS filter aggregated from the world's most trusted sources, optimized for speed and security. This list is automatically updated daily via GitHub Actions.

---

## 🚀 Key Features

* **Automated Updates:** The system automatically scans and refreshes data daily at 07:00 AM (GMT+7).
* **Extensive Coverage:** Aggregated from HaGeZi Pro+, AdGuard, hostsVN, ABPVN, and multiple Malware/Phishing protection sources.
* **Smart Exclusion:** Automatically removes domains listed in the Whitelist to prevent "False Positives" (blocking legitimate sites).
* **Optimized Format:** Specifically designed for AdGuard Home with the standard `||example.com^` syntax.

---

## 🔗 Usage Link (Import)

Copy the link below and paste it into the **DNS Blocklists** section in your AdGuard Home dashboard:

`https://raw.githubusercontent.com/hoafd/my-dns-blocklist/main/dns_filter.txt`

---

## 🛠️ Internal Workflow

1. **Collection:** A Python script fetches data from 8+ major blocklist sources.
2. **Filtering:** Removes duplicate domains and filters out entries present in the safe-list (Whitelist).
3. **Build:** Generates the latest `dns_filter.txt` file.
4. **Deploy:** GitHub Actions automatically commits and pushes the new data to the repository.

---

## ☕ Support my work

If you find this project helpful, please consider supporting me to maintain the server and develop more free tools:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-orange?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.buymeacoffee.com/hoa0290303s)

*Or scan the QR code on my profile:* [buymeacoffee.com/hoa0290303s](https://www.buymeacoffee.com/hoa0290303s)

---

## ⚖️ License
This project is licensed under the [MIT License](LICENSE). Copyright (c) 2026 **hoafd**.
