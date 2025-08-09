# LaTeX Attendee Badges

A LaTeX-based template for generating professional, event-ready name tags directly from a CSV file.

## Features
- CSV-driven: Easily update attendee data without touching LaTeX code.
- Supports first name, last name, pronouns, and affiliation.
- Modern, customizable badge design with event logo and branding.
- Flexible layout for multi-column badge sheets.
- Custom color themes using hex codes.

## Example
**Sample CSV format:**
```csv
First name,Last name,Pronouns,Affiliation
Alex,Johnson,he/him,OpenAI Research
Maria,Gonzalez,she/her,University of Barcelona
Jordan,Lee,they/them,Tech for Good Foundation
```

## Usage
1. Clone this repository:
2. Place your `attendees.csv` file in the project directory.
3. Update the LaTeX file (`badges.tex`) to match your event name, logo, and colors.
4. Compile with XeLaTeX or LuaLaTeX:
```bash
xelatex badges.tex
```
5. Print the generated PDF on the desired badge sheets.

## Customization
- **Colors:** Adjust in `\definecolor` lines.
- **Fonts:** Change via `\setmainfont` and `\setsansfont`.
- **Layout:** Modify badge size variables `\badgew` and `\badgeh`.
---
**Repository name suggestion:** `latex-attendee-badges`
