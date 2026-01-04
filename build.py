import requests
import re
from datetime import datetime

# Các nguồn blocklist
block_urls = [
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.plus.txt",
    "https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts",
    "https://abpvn.com/android/abpvn.txt",
    "https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-agh.txt",
    "https://phishing.army/download/phishing_army_blocklist_extended.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.txt",
    "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt"
]

whitelist_urls = ["https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/whitelist-referral-native.txt"]

def clean_domain(url):
    try:
        # Thêm User-Agent để giả lập trình duyệt
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=15)
        domains = set()
        for line in resp.text.splitlines():
            line = line.strip()
            if not line or line.startswith(('!', '#', '[', '@')): continue
            # Chuyển đổi format hosts/adblock về domain thuần
            domain = re.sub(r'^(0\.0\.0\.0\s+|127\.0\.0\.1\s+|\|\||\^|@@)', '', line).strip()
            if domain: domains.add(domain)
        return domains
    except Exception as e:
        print(f"Lỗi khi tải {url}: {e}")
        return set()

all_blocks = set()
for u in block_urls: 
    print(f"Đang tải blocklist: {u}")
    all_blocks.update(clean_domain(u))

all_white = set()
for u in whitelist_urls: 
    print(f"Đang tải whitelist: {u}")
    all_white.update(clean_domain(u))

# Lọc bỏ whitelist
final = all_blocks - all_white

# Ghi file
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("dns_filter.txt", "w") as f:
    f.write(f"! Title: hoafd Custom Filter\n")
    f.write(f"! Updated: {current_time} (UTC)\n")
    f.write(f"! Total domains: {len(final)}\n\n")
    for d in sorted(final):
        f.write(f"||{d}^\n")
