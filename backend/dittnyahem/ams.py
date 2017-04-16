# coding=utf-8
import requests
import random
import json
from municipalityCodes import codeToName as mCodeToName
from occupationCodes import codeToName as oCodeToName
from sfi import codeToUrl
from polisen import stationer
demoMunicipalities = [
    "0665",  # Vaggeryd (Också Hrsr_9dEIfw, eller inte.. )
    "2260",  # Ånge
    "0763",  # Tingsryd
    "2481"   # Lycksele
]

youtubeVideos = {
    "0665": "T5Vlgzqg34Y?start=7",  # Vaggeryd (Också Hrsr_9dEIfw, eller inte.. )
    "2260": "lsgJUpXmw5U?start=0",  # Ånge
    "0763": "MXsC9fsyEUI?start=0",  # Tingsryd
    "2481": "w2AX1qMFngU?start=24"  # Lycksele
}

class SFIEntry(object):
    def __init__(self, url):
        self.url = url

class Employer(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Occupation(object):
    def __init__(self, name, jobs):
        self.name = name
        self.jobs = jobs

class SearchResponse(object):
    def __init__(self, municipalName, municipalCode, employers, occupations, sfi, polis):
        self.municipalName = municipalName
        self.municipalCode = municipalCode
        if municipalName[-1] in ['x','s','a','e','u','i','ö','y','o','ä','å']:
            self.municipalNameFull = '%s kommun' % self.municipalName
        else:
            self.municipalNameFull = '%ss kommun' % self.municipalName
        swedishCharacters = [('å','a'),('ä','a'),('ö','o')]
        s = self.municipalName
        for (a,b) in swedishCharacters:
            s = s.replace(a,b)
        self.municipalURL = 'http://www.%s.se' % s
        self.employers = employers
        self.occupations = occupations
        self.sfi = sfi
        self.youtubeVideo = youtubeVideos[municipalCode]
        self.polis = polis


class AmsClient(object):
    def __init__(self):
        pass

    def parseEmployers(self, data):
        counts = data["Counts"]
        employers = data["Employers"]
        returnData = []
        for name, count in zip(employers, counts):
            returnData.append(Employer(name.encode("utf-8"), count))

        return returnData

    def parseOccupations(self, data):
        counts = data["Counts"]
        occupations = data["Occupation"]
        returnData = []
        for occupationId, count in zip(occupations, counts):
            occupationName = oCodeToName.get(occupationId, "")

            returnData.append(Occupation(occupationName, count))

        return returnData


    def search(self, keywords):
        year = 2016

        i = random.randint( 0, len(demoMunicipalities)-1 )
        kommunId = demoMunicipalities[i]

        queryString = "(%s) %s %s" % (keywords, year, kommunId)
        # Let requests encode it
        #queryString = "(f%C3%B6rsvaret%20milit%C3%A4r)%202016%202481"
        r = requests.get("http://13.74.12.222:8080/realtime1/" + queryString)
        content = json.loads(r.text)

        del content["retrieval_time"]
        rest = content.values()[0]

        employers = []
        if "employers" in rest:
            employers = self.parseEmployers(rest["employers"])
        occupations = []
        if "occupations" in rest:
            occupations = self.parseOccupations(rest["occupations"])

        mName = mCodeToName.get(int(kommunId), "").capitalize()
        sr = SearchResponse(
            mName,
            kommunId,
            employers,
            occupations,
            SFIEntry(codeToUrl.get(int(kommunId), SFIEntry(""))),
            stationer.get(mName.lower(), False)
        )

        return sr


if __name__ == '__main__':
    ams = AmsClient()
    ams.search("")





