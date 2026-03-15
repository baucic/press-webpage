import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader("templates"))

with open("article/db.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

Path("dist").mkdir(exist_ok=True)

for page in ["archive", "events", "places", "index"]:
    template = env.get_template(f"{page}.html")
    html = template.render(articles=articles)

    with open(f"{page}.html", "w", encoding="utf-8") as f:
        f.write(html)
