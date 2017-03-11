# coding=utf-8
import requests
import json
from municipalityCodes import codeToName as mCodeToName
from occupationCodes import codeToName as oCodeToName
from sfi import codeToUrl

group = "administration ekonomi Industriell tillverkning"

demoTime = {
    "0665": "",  # Vaggeryd (Också Hrsr_9dEIfw, eller inte.. )
    "2260": "",  # Ånge
    "0763": "",  # Tingsryd
    "2481": ""  # Lycksele
}

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
    def __init__(self, municipalName, municipalCode, employers, occupations, sfi):
        self.municipalName = municipalName
        self.municipalCode = municipalCode
        self.employers = employers
        self.occupations = occupations
        self.sfi = sfi
        self.youtubeVideo = youtubeVideos[municipalCode]


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


    def search(self):
        year = 2016

        kommunId = '2481'

        queryString = "(%s) %s %s" % (group, year, kommunId)
        # Let requests encode it
        r = requests.get("http://13.74.12.222:8080/realtime1/" + queryString)
        content = json.loads(r.text)

        del content["retrieval_time"]
        rest = content.values()[0]

        employers = self.parseEmployers(rest["employers"])
        occupations = self.parseOccupations(rest["occupations"])

        data = rest["kommunkoder_total"]

        result = {}
        # Pull out only the ones that has a value
        for code, amount in data.iteritems():
            code = long(code)
            amount = long(amount)
            if amount > 0:
                name = mCodeToName.get(code, "")
                result[name] = amount


        sr = SearchResponse(
            mCodeToName.get(int(kommunId), "").capitalize(),
            kommunId,
            employers,
            occupations,
            SFIEntry(codeToUrl.get(int(kommunId), SFIEntry("")))
        )

        return sr


if __name__ == '__main__':
    ams = AmsClient()
    ams.search()





