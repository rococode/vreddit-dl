#!/usr/bin/env python

# example:
# ./vdl.py https://old.reddit.com/r/funny/comments/a27fhv/elmos_voice_saying_ill_fk_you_up_is_the_best_and/

import os
import sys
import urllib2
from bs4 import BeautifulSoup
import youtube_dl

OUT_DIR = "./out"

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

if len(sys.argv) != 2:
    print "Use as ./vdl.py <url>"
    sys.exit(1)

urls = []
url = sys.argv[1]

if url.endswith(".mpd"):
    urls.append(url)
else:
    print "\nFetching " + url + "..."
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    response = opener.open(url)
    soup = BeautifulSoup(response, 'html.parser')
    for e in soup.find_all():
        if 'data-mpd-url' in e.attrs:
            urls.append(e.attrs['data-mpd-url'].encode('ascii', 'ignore'))
    print "Found {} URL{}!".format(len(urls), '' if len(urls) is 1 else 's')

for u in urls:
    print "Downloading {}...".format(u)
    ydl_opts = {
        'outtmpl': OUT_DIR + os.sep + '%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print "dl " + u
        ydl.download([u])

print "Done!"
