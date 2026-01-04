# 🚫 My DNS Blocklist

Danh sách các tên miền quảng cáo, theo dõi và nội dung độc hại được cập nhật thủ công nhằm tối ưu hóa trải nghiệm duyệt web, đặc biệt là các trang web tại Việt Nam.

---

## 🚀 Cách sử dụng

Để sử dụng bộ lọc này, bạn hãy sao chép đường dẫn bên dưới và dán vào phần cấu hình Blocklist của **AdGuard Home**, **Pi-hole** hoặc các ứng dụng hỗ trợ chặn DNS.

### Link Raw (Sử dụng link này):
`https://raw.githubusercontent.com/hoafd/my-dns-blocklist/main/dns_filter.txt`

---

## 🛠️ Hướng dẫn thêm vào AdGuard Home

1. Mở giao diện quản trị **AdGuard Home**.
2. Chọn menu **Filters** (Bộ lọc) -> **DNS Blocklists**.
3. Nhấn nút **Add blocklist** -> **Add a custom list**.
4. Nhập tên: `hoafd Personal Filter`.
5. Dán đường dẫn URL ở trên vào ô tương ứng.
6. Nhấn **Save** (Lưu).

---

## 📝 Định dạng bản ghi
Bộ lọc sử dụng định dạng tiêu chuẩn của AdGuard/Hosts:
- `||example.com^`: Chặn toàn bộ tên miền example.com và các tên miền con.
- `0.0.0.0 ads.example.com`: Trỏ tên miền quảng cáo về IP trống.

---

## ⚖️ Giấy phép (License)
Dự án này được cấp phép theo [MIT License](LICENSE). Copyright (c) 2026 **hoafd**.
