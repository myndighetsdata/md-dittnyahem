# coding=utf-8
group = "administration ekonomi Industriell tillverkning"

source = {
"work0": "administration ekonomi",
"work1": "bygg anläggning",
"work2": "data it systemutvecklare",
"work3": "försäljning inköp marknadsföring",
"work4": "hantverk",
"work5": "hotell restaurang kök",
"work6": "sjukvård hälsovård vårdcentral hälsocentral",
"work7": "tillverkning industri industriell",
"work8": "installation drift underhåll",
"work9": "skönhetsvård apotek frisör",
"work10": "kultur design grafik",
"work11": "försvaret militär",
"work12": "naturbruk",
"work13": "naturvetenskap fysik kemist forskare",
"work14": "förskolelärare lärare rektor",
"work15": "städare sanering återvinning sotning",
"work16": "kurator diakon präst kyrkan socionom undersköterska pedagog",
"work17": "brand polis väktare räddningsledare",
"work18": "arkitekt ingengör gis tandläkare",
"work19": "transport truckförare förare brevbärare"
}

def getGroupString(formData):
    result = []
    for key in source.keys():
        entry = formData.get(key, None)

        if entry:
            result.append(source.get(key))

    return " ".join(result)
