import requests
from datetime import datetime

r = requests.get("https://www.tn.gov/health/cedep/ncov.html")
body = r.text[r.text.find('<p>County</p>'):]
body = body.split("<tr")
total = 0
f = open('convid_tn.csv', "a")

for line in body:
    if "<th>" in line or "<tbody>" in line:
        continue
    cell = line.split("<td")
    county = cell[1][cell[1].find("<p>")+3:cell[1].find("</p>")]
    num = cell[2][cell[2].find("<p>")+3:cell[2].find("</p>")]
    timestampStr = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    total += int(num)
    output = f"\"{datetime.now()}\", \"{county}\", {num}\r\n"
    print(output)
    f.write(output)
    
print(total)
f.close()


