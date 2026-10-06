from pathlib import Path

OUTPUT_FILE = Path("assets/ascii.svg")

svg = r'''
<svg xmlns="http://www.w3.org/2000/svg"
     width="500"
     height="500"
     viewBox="0 0 500 500">

<style>

.ascii {
    font-family: monospace;
    font-size: 7px;
    fill: #39d353;
    letter-spacing: 1px;
}

.container {
    animation: fadeIn 1.5s ease-out forwards;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scale(0.95);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

</style>

<rect
    width="500"
    height="500"
    rx="16"
    fill="#05070d"
/>

<g class="container">

<text x="30" y="45" class="ascii">
+--------------------------------------+
</text>

<text x="30" y="70" class="ascii">
|        SUMIT KUMAR // DEV             |
</text>

<text x="30" y="95" class="ascii">
+--------------------------------------+
</text>

<text x="80" y="150" class="ascii">
        █████████████
</text>

<text x="70" y="165" class="ascii">
      █████████████████
</text>

<text x="65" y="180" class="ascii">
     ████       ████
</text>

<text x="60" y="195" class="ascii">
    ███           ███
</text>

<text x="60" y="210" class="ascii">
    ███    ███    ███
</text>

<text x="65" y="225" class="ascii">
     ███       ███
</text>

<text x="70" y="240" class="ascii">
      █████████████
</text>

<text x="80" y="255" class="ascii">
        █████████
</text>

<text x="55" y="300" class="ascii">
        SOFTWARE ENGINEER
</text>

<text x="75" y="325" class="ascii">
        AI / ML • BACKEND
</text>

<text x="100" y="350" class="ascii">
        FULL STACK DEV
</text>

<text x="30" y="400" class="ascii">
$ echo "keep building 🚀"
</text>

<text x="30" y="430" class="ascii">
$ status: ONLINE
</text>

</g>

</svg>
'''

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(svg)

print(f"Created {OUTPUT_FILE}")
