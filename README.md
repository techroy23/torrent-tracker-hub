# Torrent Tracker Hub

Aggregated torrent tracker list from multiple sources.

## Sources

1. **ngosang/trackerslist**
   - URL: https://github.com/ngosang/trackerslist
   - Files: `trackers_all.txt`, `trackers_all_ip.txt`

2. **trackerslist.com**
   - URL: https://trackerslist.com/
   - Files: `best.txt`, `all.txt`, `http.txt`, `nohttp.txt`

3. **lighting9999/tracker-project**
   - URL: https://github.com/lighting9999/tracker-project
   - Files: `trackers_all.txt`, `trackers_best.txt`, `trackers_best_dual.txt`, `trackers_best_http.txt`, `trackers_best_https.txt`, `trackers_best_ipv4.txt`, `trackers_best_ipv6.txt`, `trackers_best_udp.txt`, `trackers_best_ws.txt`, `trackers_best_wss.txt`

4. **NewTrackon**
   - URL: https://newtrackon.com/
   - API: `https://newtrackon.com/api/all`

5. **Trackers.run**
   - URL: https://trackers.run/
   - File: `wp_ws_up_hp_hs_v4_v6.txt`

## Download Raw Files

Direct download links (use in torrent clients):

| File | Raw URL |
|------|---------|
| All Trackers | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_all.txt |
| HTTP Only | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_http.txt |
| HTTPS Only | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_https.txt |
| UDP Only | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_udp.txt |
| WebSocket | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_ws.txt |

## Usage

Run locally:
```bash
pip install fake-useragent python-dotenv
cp .env.example .env
# Add your GH_PAT to .env
python scripts/download_trackers.py
```

## Output

Output files in `output/`:
- `trackers_all.txt` - All trackers (sorted, deduplicated)
- `trackers_http.txt` - HTTP trackers only
- `trackers_https.txt` - HTTPS trackers only
- `trackers_udp.txt` - UDP trackers only
- `trackers_ws.txt` - WebSocket trackers (ws://, wss://)

All files have blank lines between entries.

## GitHub Actions

The workflow runs automatically on push to main and hourly via schedule.

## License

This project aggregates public tracker lists. Each source maintains its own license.