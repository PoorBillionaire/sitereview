# sitereview
Bluecoat SiteReview Checker (CLI)

# Description

Site Review can best be described by Blue Coat itself:

*The purpose of Site Review is to allow Blue Coat customers to check the current categorization of WebPulse URL ratings and report sites that they believe are incorrectly categorized.*

This Python script focuses on the first portion, allowing Blue Coat customers to quickly query the Site Review service via the CLI.

# Usage

Sitereview.py simply takes one mandatory positional argument, url, and submits it to the Site Review service:

```
usage: sitereview.py [-h] url

positional arguments:
  url         Submit domain/URL to BlueCoat's SiteReview

optional arguments:
  -h, --help  show this help message and exit
```

