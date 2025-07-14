#!/usr/bin/env python3
import csv
import os
import subprocess
from datetime import date
from jinja2 import Environment, FileSystemLoader

# ── CONFIG ─────────────────────────────────────────────────────────────────────
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "../templates")
OUTPUT_DIR   = os.path.join(os.path.dirname(__file__), "../output")
DATA_FILE    = os.path.join(os.path.dirname(__file__), "../data/participants.csv")

EVENT_NAME     = "PyCon Europe 2025"
EVENT_DATE     = "August 12–14, 2025"
EVENT_LOCATION = "Berlin, Germany"
ORGANIZER_NAME = "PyCon Europe Org Team"

LOGO_PATH      = os.path.abspath(os.path.join(TEMPLATE_DIR, "logo.png"))
SIGNATURE_PATH = os.path.abspath(os.path.join(TEMPLATE_DIR, "signature.png"))
# ────────────────────────────────────────────────────────────────────────────────

def main():
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("confirmation.md.j2")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    today = date.today().strftime("%B %d, %Y")

    with open(DATA_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # render markdown
            md = template.render(
                first_name=row["first_name"],
                last_name =row["last_name"],
                event_name     = EVENT_NAME,
                event_date     = EVENT_DATE,
                event_location = EVENT_LOCATION,
                organizer_name = ORGANIZER_NAME,
                issue_date     = today,
                logo_path      = LOGO_PATH,
                signature_path = SIGNATURE_PATH,
            )
            fname_base = f"{row['first_name']}_{row['last_name']}".replace(" ", "_")
            md_file = os.path.join(OUTPUT_DIR, fname_base + ".md")
            pdf_file = os.path.join(OUTPUT_DIR, fname_base + ".pdf")
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(md)
            # convert to PDF via pandoc (requires pandoc + a PDF engine installed)
            subprocess.run([
                "pandoc", md_file,
                "--pdf-engine=xelatex",
                "-o", pdf_file
            ], check=True)
            print(f"→ Generated {pdf_file}")

if __name__ == "__main__":
    main()

