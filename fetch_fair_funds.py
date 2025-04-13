import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.sec.gov/divisions/enforce/claims/claimsfairfund.htm"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.select("table tr")[1:]  # skip header
claims = []

for row in rows:
    cols = row.find_all("td")
    if len(cols) < 2: continue
    name = cols[0].get_text(strip=True)
    status = cols[1].get_text(strip=True)
    claims.append({
        "project": name,
        "status": status,
        "liabilities": "Unknown",
        "opportunity": "Medium"
    })

with open("claims.json", "w") as f:
    json.dump(claims, f, indent=2)
