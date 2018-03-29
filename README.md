# sitereview
Symantec Site Review Checker (CLI)

### Description

Site Review described by Symantec:

*"Site Review allows users to check and dispute the current WebPulse categorization for any URL"*

https://sitereview.bluecoat.com/

This Python script focuses on the first portion, allowing Users to quickly query the Site Review service via the CLI. This script can be run stand-alone, or imported as a module to extend the functionality of another script.

### Usage

Sitereview.py takes one mandatory positional argument, url, and submits it to the Site Review service:

```
usage: sitereview.py [-h] url

positional arguments:
  url         Submit domain/URL to Symantec's Site Review Service

optional arguments:
  -h, --help  show this help message and exit
```

### Results

Sample results, for a known-malicious domain:

```
======================
Symantec Site Review
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
* lxml

