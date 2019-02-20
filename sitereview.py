from __future__ import print_function

import sys
import json
import requests
import xml.etree.ElementTree as ET
from argparse import ArgumentParser


class SiteReview(object):
    def __init__(self):
        self.baseurl = "https://sitereview.bluecoat.com/resource/lookup"
        self.headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

    def sitereview(self, url):
        payload = {"url": url, "captcha":""}
        self.req = requests.post(
            self.baseurl,
            headers=self.headers,
            data=json.dumps(payload)
        )
        return self.req.content.decode("UTF-8")

    def check_response(self, response):
        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} returned".format(req.status_code))
        else:
            root = ET.fromstring(self.req.content)
            self.url = root.find('.//url').text
            self.category = root.find('.//translatedCategories/en/name').text
            if root.find('.//ratingDts').text == "OLDER":
                self.date = ">"
            else:
                self.date = "<"
            self.maxdate = root.find('.//ratingDtsCutoff').text




def main(url):
    s = SiteReview()
    response = s.sitereview(url)
    s.check_response(response)
    border = "=" * (len("Symantec Site Review") + 2)

    print("\n{0}\n{1}\n{0}\n".format(border, "Symantec Site Review"))
    print("URL: {}\nLast Time Rated/Reviewed: {} {} days ago\nCategory: {}\n".format(
        s.url,
        s.date,
        s.maxdate,
        s.category
        )
    )


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("url", help="Submit domain/URL to Symantec's Site Review")
    args = p.parse_args()

    main(args.url)
