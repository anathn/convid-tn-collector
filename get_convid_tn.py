import requests
from datetime import datetime

r = requests.get("https://www.tn.gov/health/cedep/ncov.html")

marker = '<b>County</b>'

if marker not in r.text:
    marker = '<p>County</p>'

body = r.text[r.text.find(marker):]
body = body.split("<tr")
total = 0
f = open('convid_tn.csv', "a")
for line in body:
    if "<th>" in line or "<tbody>" in line or "</th>" in line:
        continue
    if "</tbody>" in line:
        break
    cell = line.split("<td")
    
    county = cell[1][cell[1].find("<p>")+3:cell[1].find("</p>")]
    num = cell[2][cell[2].find("<p>")+3:cell[2].find("</p>")]
    timestampStr = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
    try:
        total += int(num)
    except:
        # We just display this - who cares if it fails
        print("Error converging {0} to int".format(num))
    
    output =  '"{0}", "{1}", {2}\n'.format(timestampStr, county, num)

    print(output)
    f.write(output)
    
print(total)
f.close()


