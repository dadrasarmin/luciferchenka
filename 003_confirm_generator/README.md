# Confirmation Generator

This repo automates the creation of “Confirmation of Attendance” letters for event participants.

## Requirements

- Python 3.7+
- `pip install jinja2`
- [Pandoc](https://pandoc.org/) + LaTeX (for PDF output)

## Setup

1. Clone this repo  
2. Populate `data/participants.csv` with your attendees  
3. Replace `templates/logo.png`, `templates/signature.png`  
4. Edit `templates/confirmation.md.j2` to suit your event  
5. Run:

   ```bash
   cd scripts
   python generate.py

