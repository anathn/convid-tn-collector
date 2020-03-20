import requests
from datetime import datetime

r = requests.get("https://www.tn.gov/health/cedep/ncov.html")
body = r.text.split("<tr>")
total = 0
for line in body:
    row = line[:line.find("</tr>")]
    if "bottom" in row:
        cell = row.split("</td>")
        county = cell[0][cell[0].find("<p>")+3:cell[0].find("</p>")]
        num = cell[1][cell[1].find("<p>")+3:cell[1].find("</p>")]
        total += int(num)
        output = f"\"{datetime.now()}\", \"{county}\", {num}\r\n"
        with open('convid_tn.csv', "a") as f:
            f.write(output)

print(total)
