from __future__ import print_function

from argparse import ArgumentParser
from bs4 import BeautifulSoup
import json
import requests
import sys


class SiteReview(object):
    def __init__(self):
        self.baseurl = "https://sitereview.bluecoat.com/resource/lookup"
        self.headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

    def sitereview(self, url):
        payload = {"url": url, "captcha":""}
        
        try:
            self.req = requests.post(
                self.baseurl,
                headers=self.headers,
                data=json.dumps(payload),
            )
        except requests.ConnectionError:
            sys.exit("[-] ConnectionError: " \
                     "A connection error occurred")

        return json.loads(self.req.content.decode("UTF-8"))

    def check_response(self, response):
        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} returned".format(req.status_code))
        else:
            self.category = response["categorization"][0]["name"]
            self.date = response["translatedRateDates"][0]["text"][0:35]
            self.url = response["url"]



def main(url):
    s = SiteReview()
    response = s.sitereview(url)
    s.check_response(response)
    border = "=" * (len("Symantec Site Review") + 2)

    print("\n{0}\n{1}\n{0}\n".format(border, "Symantec Site Review"))
    print("URL: {}\n{}\nCategory: {}\n".format(
        s.url,
        s.date,
        s.category
        )
    )


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("url", help="Submit domain/URL to Symantec's Site Review")
    args = p.parse_args()

    main(args.url)
