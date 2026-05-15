import urllib.request
import os
from collections import OrderedDict
from datetime import datetime
from fake_useragent import UserAgent
from dotenv import load_dotenv

load_dotenv()

URLS = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt",
    "https://cf.trackerslist.com/best.txt",
    "https://cf.trackerslist.com/all.txt",
    "https://cf.trackerslist.com/http.txt",
    "https://cf.trackerslist.com/nohttp.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_all.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_dual.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_http.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_https.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_ipv4.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_ipv6.txt",
    "http://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_udp.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_ws.txt",
    "https://raw.githubusercontent.com/lighting9999/tracker-project/refs/heads/master/trackers_best_wss.txt",
    "https://newtrackon.com/api/all",
    "https://trackers.run/s/wp_ws_up_hp_hs_v4_v6.txt"
]
OUTPUT_DIR = "output"

GH_PAT = os.getenv("GH_PAT")

ua = UserAgent()
headers = {"User-Agent": ua.random}

def fetch_url(url):
    req = urllib.request.Request(url, headers=headers)
    if "raw.githubusercontent.com" in url and GH_PAT:
        req.add_header("Authorization", f"token {GH_PAT}")
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

def categorize_trackers(trackers):
    http_trackers = []
    https_trackers = []
    udp_trackers = []
    ws_trackers = []

    for tracker in trackers:
        lower = tracker.lower()
        if lower.startswith("http://"):
            http_trackers.append(tracker)
        elif lower.startswith("https://"):
            https_trackers.append(tracker)
        elif lower.startswith("udp://"):
            udp_trackers.append(tracker)
        elif lower.startswith("ws://") or lower.startswith("wss://"):
            ws_trackers.append(tracker)

    return {
        "http": sorted(http_trackers),
        "https": sorted(https_trackers),
        "udp": sorted(udp_trackers),
        "ws": sorted(ws_trackers)
    }

def write_trackers(trackers, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for i, tracker in enumerate(trackers):
            f.write(tracker + "\n")
            if i < len(trackers) - 1:
                f.write("\n")

def write_whitelist(whitelist, filename):
    date = datetime.now().strftime("%m-%d-%Y")
    header = f"[Adblock Plus]\n! Title: Techroy23 Torrent Tracker Whitelist\n! Description: Whitelisted domains\n! Homepage: https://github.com/techroy23/torrent-tracker-hub\n! Updated: {date}\n"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(whitelist))

def create_whitelist(trackers):
    whitelist = []
    seen = set()
    for tracker in trackers:
        host = tracker.split("://")[1] if "://" in tracker else tracker
        host = host.split("/")[0]
        if host.startswith("["):
            continue
        if ":" in host:
            host = host.split(":")[0]
        if host and not host[0].isdigit():
            entry = f"@@||{host}^$important"
            if entry not in seen:
                seen.add(entry)
                whitelist.append(entry)
        elif host and not any(c.isalpha() for c in host.split(".")[0] if host):
            continue
    return sorted(whitelist)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    trackers = []
    for url in URLS:
        try:
            content = fetch_url(url)
            trackers.extend(line.strip() for line in content.splitlines() if line.strip())
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    unique_trackers = list(OrderedDict.fromkeys(trackers))
    unique_trackers.sort()

    write_trackers(unique_trackers, f"{OUTPUT_DIR}/trackers_all.txt")
    print(f"Wrote {len(unique_trackers)} trackers to {OUTPUT_DIR}/trackers_all.txt")

    categorized = categorize_trackers(unique_trackers)

    write_trackers(categorized["http"], f"{OUTPUT_DIR}/trackers_http.txt")
    print(f"Wrote {len(categorized['http'])} trackers to {OUTPUT_DIR}/trackers_http.txt")

    write_trackers(categorized["https"], f"{OUTPUT_DIR}/trackers_https.txt")
    print(f"Wrote {len(categorized['https'])} trackers to {OUTPUT_DIR}/trackers_https.txt")

    write_trackers(categorized["udp"], f"{OUTPUT_DIR}/trackers_udp.txt")
    print(f"Wrote {len(categorized['udp'])} trackers to {OUTPUT_DIR}/trackers_udp.txt")

    write_trackers(categorized["ws"], f"{OUTPUT_DIR}/trackers_ws.txt")
    print(f"Wrote {len(categorized['ws'])} trackers to {OUTPUT_DIR}/trackers_ws.txt")

    whitelist = create_whitelist(unique_trackers)
    write_whitelist(whitelist, f"{OUTPUT_DIR}/whitelist.txt")
    print(f"Wrote {len(whitelist)} entries to {OUTPUT_DIR}/whitelist.txt")

if __name__ == "__main__":
    main()