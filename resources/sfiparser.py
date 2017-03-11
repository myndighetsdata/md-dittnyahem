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

with open("sfi.py", "wb") as fp:

    fp.write("codeToUrl = {\n")
    for line in rest:
        content = line.split("|")
        municipalCode = long(content[4])
        url = content[15]
        fp.write("%s: \"%s\",\n" % (municipalCode, url))
    fp.write("}\n")



