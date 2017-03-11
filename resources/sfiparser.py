import json

"""
Reads the sfi csv and generates a json

"""

data = open("sfi.csv").read()
data = data.split("\n")
header = data[0]
rest = data[1:]

headerParts = header.split(",")

output = []
for line in rest:

    content = line.split("|")
    municipalCode = long(content[4])
    url = content[15]


    output.append({
        "municipalCode": municipalCode,
        "url": url
    })

open("sfi.json", "wb").write(json.dumps(output))

