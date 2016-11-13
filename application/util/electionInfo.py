import requests
import urllib
import pprint


class ElectionInfo:

    def __init__(self, key):
        self.key = key
        self.baseurl = "https://www.googleapis.com/civicinfo/v2"

    def get_elections(self):
        electionUrl = "{0}/elections?key={1}".format(self.baseurl, self.key)
        return requests.get(electionUrl).json()['elections']

    def get_voterInfo(self, address, id):
        safeAddress = urllib.quote(address)
        try:
            voterUrl = "{0}/voterinfo?key={1}&address={2}".format(self.baseurl, self.key, safeAddress)
            res = requests.get(voterUrl)
            if res.status_code >= 400:
                raise
            res = res.json()
        except:
            voterUrl = "{0}/voterinfo?key={1}&address={2}&electionId={3}".format(self.baseurl, self.key, safeAddress, id)
            res = requests.get(voterUrl).json()
        return res['contests']




def main():
    elect = ElectionInfo("AIzaSyBcM1yBZ6R7Bva6xnluLFL6L_bzhHiU_Sw")
    res = elect.get_voterInfo("101 Chestnut St. Berea City KY", 2000)

if __name__ == "__main__":
    main()
