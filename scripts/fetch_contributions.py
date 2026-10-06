import json
import re
import urllib.request
from datetime import datetime, timezone

USERNAME = "Sumitkumar136"
OUTPUT_FILE = "data/contributions.json"

url = f"https://github.com/users/{USERNAME}/contributions"

request = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

with urllib.request.urlopen(request) as response:
    html = response.read().decode("utf-8")

pattern = re.compile(
    r'<td[^>]*data-date="([^"]+)"[^>]*data-level="(\d+)"[^>]*>'
)

contributions = []

for date, level in pattern.findall(html):
    contributions.append({
        "date": date,
        "level": int(level)
    })

data = {
    "username": USERNAME,
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "contributions": contributions
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)

print(f"Saved {len(contributions)} contribution days.")
