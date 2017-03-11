from lxml import etree
import io
path = "talsvarxml.xml"
output = ""

with open(path, "rb") as fp:
    output = io.BytesIO(fp.read())

root = etree.parse(output).getroot()

with open("polisen.py", "wb") as fp:
    fp.write("stationer = {\n")

    for kommun in root.getiterator("kommun"):
        name = kommun.attrib["namn"]
        name = name.encode("utf8")
        fp.write("\"%s\": \"%s\",\n" % (name.lower(), name))

    fp.write("}\n")