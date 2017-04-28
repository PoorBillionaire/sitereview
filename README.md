# sitereview
Blue Coat Site Review Checker (CLI)

### Description

Site Review can best be described by Blue Coat itself:

*"The purpose of Site Review is to allow Blue Coat customers to check the current categorization of WebPulse URL ratings and report sites that they believe are incorrectly categorized."*

https://sitereview.bluecoat.com/sitereview.jsp

This Python script focuses on the first portion, allowing Blue Coat customers to quickly query the Site Review service via the CLI. This script can be run stand-alone, or imported as a module to extend the functionality of another script.

### Usage

Sitereview.py simply takes one mandatory positional argument, url, and submits it to the Site Review service:

```
usage: sitereview.py [-h] url

positional arguments:
  url         Submit domain/URL to Blue Coat's Site Review

optional arguments:
  -h, --help  show this help message and exit
```

### Results

Sample results, for a known-malicious domain:

```
======================
Blue Coat Site Review
======================

URL: http://brins.biz/
Last Time Rated/Reviewed:  > 7 days
Category: Malicious Sources/Malnets
```

### Python Requirements

* argparse
* bs4
* json
* requests
* sys

