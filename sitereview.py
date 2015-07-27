from argparse import ArgumentParser
from bs4 import BeautifulSoup
import json
import requests
import sys


class SiteReview(object):
    def __init__(self):
        self.baseurl = "http://sitereview.bluecoat.com/rest/categorization"
        self.useragent = {"User-Agent": "Mozilla/5.0"}

    def sitereview(self, url):
        payload = {"url": url}
        
        try:
            self.req = requests.post(
                                    self.baseurl,
                                    headers=self.useragent,
                                    data=payload
                                    )
        except requests.ConnectionError:
            sys.exit("[-] ConnectionError: " \
                     "A connection error occurred")

        return json.loads(self.req.content)

    def check_response(self, response):

        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} returned".format(req.status_code))

        elif "error" in response:
            sys.exit(response["error"])

        else:
            self.category = BeautifulSoup(response["categorization"]).get_text()
            self.date = BeautifulSoup(response["ratedate"]).get_text()[0:35]
            self.url = response["url"]


def main(url):
    s = SiteReview()
    response = s.sitereview(url)
    s.check_response(response)
    border = "=" * (len("BlueCoat Site Review") + 2)

    print "\n{0}\n{1}\n{0}\n".format(border, "BlueCoat Site Review")
    print "URL: {}\nLast Reviewed: {}\nCategory: {}\n".format(
                                                              s.url,
                                                              s.date,
                                                              s.category
                                                              )


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("url", help="Submit domain/URL to BlueCoat's SiteReview")
    args = p.parse_args()

    main(args.url)

else:
    pass
