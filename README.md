# 🚫 My DNS Blocklist (Auto-Updated)

Bộ lọc DNS cá nhân được tổng hợp từ các nguồn uy tín nhất thế giới, tối ưu hóa cho tốc độ và bảo mật. Danh sách này được tự động cập nhật hàng ngày bằng GitHub Actions.



---

## 🚀 Tính năng nổi bật

* **Tự động cập nhật:** Hệ thống tự động quét và cập nhật dữ liệu mới nhất vào lúc 07:00 AM (giờ Việt Nam) hàng ngày.
* **Độ bao phủ cao:** Tổng hợp từ HaGeZi Pro+, AdGuard, hostsVN, ABPVN, và nhiều nguồn chống Malware/Phishing khác.
* **Loại trừ thông minh:** Tự động loại bỏ các tên miền nằm trong Whitelist để tránh tình trạng "chặn nhầm" (False Positive).
* **Định dạng tối ưu:** Chuyên dụng cho AdGuard Home với định dạng `||example.com^`.

---

## 🔗 Link sử dụng (Import)

Hãy copy link dưới đây và dán vào phần **DNS Blocklists** trong AdGuard Home:

`https://raw.githubusercontent.com/hoafd/my-dns-blocklist/main/dns_filter.txt`

---

## 🛠️ Quy trình vận hành (Workflow)

1. **Thu thập:** Script Python tải dữ liệu từ 8+ nguồn blocklist lớn.
2. **Lọc:** Loại bỏ các tên miền trùng lặp và các tên miền nằm trong danh sách an toàn (Whitelist).
3. **Build:** Xuất bản file `dns_filter.txt` mới.
4. **Deploy:** GitHub Action tự động Commit và Push dữ liệu mới lên Repository.

---

## ☕ Support my work

Nếu bạn thấy các dự án này hữu ích, bạn có thể ủng hộ tôi để duy trì server và phát triển thêm nhiều công cụ miễn phí khác:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-orange?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://www.buymeacoffee.com/hoa0290303s)

*Hoặc quét mã QR qua trang cá nhân:* [buymeacoffee.com/hoa0290303s](https://www.buymeacoffee.com/hoa0290303s)

---

## ⚖️ Giấy phép
Dự án được cấp phép theo [MIT License](LICENSE). Copyright (c) 2026 **hoafd**.
