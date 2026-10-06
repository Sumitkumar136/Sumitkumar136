import json
from pathlib import Path

DATA_FILE = Path("data/contributions.json")
OUTPUT_FILE = Path("assets/contributions.svg")

CELL_SIZE = 12
GAP = 3
PADDING = 20

with open(DATA_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

contributions = data.get("contributions", [])

# Sort contributions by date
contributions.sort(key=lambda x: x["date"])

# Keep latest 365 days
contributions = contributions[-365:]

# Create 7 rows × required weeks
weeks = []

for i in range(0, len(contributions), 7):
    week = contributions[i:i + 7]

    while len(week) < 7:
        week.append({
            "date": "",
            "level": 0
        })

    weeks.append(week)

width = PADDING * 2 + len(weeks) * (CELL_SIZE + GAP)
height = PADDING * 2 + 7 * (CELL_SIZE + GAP) + 25

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
        transform-box: fill-box;
        transform-origin: center;
        animation: appear 0.8s ease-out forwards;
        opacity: 0;
    }}

    @keyframes appear {{
        from {{
            opacity: 0;
            transform: scale(0.3);
        }}

        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
</style>

<rect
    width="100%"
    height="100%"
    rx="12"
    fill="#05070d"
/>

<text
    x="{PADDING}"
    y="18"
    class="title">
    $ github contributions --user {data.get("username", "Sumitkumar136")}
</text>
'''

for week_index, week in enumerate(weeks):

    for day_index, item in enumerate(week):

        level = int(item.get("level", 0))

        x = PADDING + week_index * (CELL_SIZE + GAP)
        y = 30 + day_index * (CELL_SIZE + GAP)

        opacity = {
            0: 0.08,
            1: 0.25,
            2: 0.45,
            3: 0.70,
            4: 1.00
        }.get(level, 0.08)

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
