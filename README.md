# Torrent Tracker Hub

[![Download Trackers](https://github.com/techroy23/torrent-tracker-hub/actions/workflows/download-trackers.yml/badge.svg)](https://github.com/techroy23/torrent-tracker-hub/actions/workflows/download-trackers.yml)

Aggregated torrent tracker lists from multiple sources. Updated automatically via GitHub Actions.

## Download Links

| Type | URL |
|------|-----|
| All Trackers | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_all.txt |
| HTTP | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_http.txt |
| HTTPS | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_https.txt |
| UDP | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_udp.txt |
| WebSocket | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/trackers_ws.txt |
| Whitelist | https://raw.githubusercontent.com/techroy23/torrent-tracker-hub/main/output/whitelist.txt |

## Sources

- [ngosang/trackerslist](https://github.com/ngosang/trackerslist)
- [trackerslist.com](https://trackerslist.com/)
- [lighting9999/tracker-project](https://github.com/lighting9999/tracker-project)
- [NewTrackon](https://newtrackon.com/)
- [Trackers.run](https://trackers.run/)

## Whitelist

The `whitelist.txt` file contains AdBlock-compatible allowlist entries for torrent trackers.

### Supported Applications

- uBlock Origin / uBlock Origin Lite
- AdGuard Browser Assistant
- AdGuard DNS, NextDNS, Control D and other DNS apps

## Local Usage

```bash
pip install fake-useragent python-dotenv
cp .env.example .env
# Add your GH_PAT to .env
python scripts/download_trackers.py
```

## GitHub Actions

The workflow runs:
- On every push to main
- Hourly on schedule
- Manually via workflow dispatch

## License

This project aggregates public tracker lists. Each source maintains its own license.