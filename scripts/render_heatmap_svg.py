import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("assets/contributions.svg")

CELL_SIZE = 12
GAP = 3
PADDING = 20

LEVEL_CHARS = {
    0: " ",
    1: "░",
    2: "▒",
    3: "▓",
    4: "█",
}

with open(DATA_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

contributions = data.get("contributions", [])

# Last 365 days
contributions = contributions[-365:]

if not contributions:
    contributions = [
        {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "level": 0
        }
    ]

weeks = []
current_week = []

for item in contributions:
    current_week.append(item)

    if len(current_week) == 7:
        weeks.append(current_week)
        current_week = []

if current_week:
    weeks.append(current_week)

width = PADDING * 2 + len(weeks) * (CELL_SIZE + GAP)
height = PADDING * 2 + 7 * (CELL_SIZE + GAP) + 30

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<style>
    .title {{
        font-family: monospace;
        font-size: 14px;
        fill: #ffffff;
    }}

    .cell {{
        animation: appear 0.8s ease-out forwards;
        opacity: 0;
    }}

    @keyframes appear {{
        from {{
            opacity: 0;
            transform: scale(0.4);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
</style>

<rect width="100%" height="100%" fill="#05070d" rx="12"/>

<text x="{PADDING}" y="18" class="title">
    $ github contributions --user {data.get("username", "Sumitkumar136")}
</text>
'''

for week_index, week in enumerate(weeks):

    for day_index, item in enumerate(week):

        level = int(item.get("level", 0))

        x = PADDING + week_index * (CELL_SIZE + GAP)
        y = 30 + day_index * (CELL_SIZE + GAP)

        opacity = 0.15 + (level * 0.2)

        delay = (week_index * 7 + day_index) * 0.01

        svg += f'''
<rect
    x="{x}"
    y="{y}"
    width="{CELL_SIZE}"
    height="{CELL_SIZE}"
    rx="2"
    fill="#39d353"
    opacity="{opacity}"
    class="cell"
    style="animation-delay:{delay}s"
/>
'''

svg += "</svg>"

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(svg)

print(f"Created {OUTPUT_FILE}")
