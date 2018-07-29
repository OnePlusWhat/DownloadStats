#!/usr/bin/env python3

# pylint: disable=not-callable

"""
DownloadStats: Pull statistics about download counts of GitHub releases
of specified projects
"""
import io
import sys

from future.types.newstr import unicode

try:
    import requests
except ImportError:
    print("Error: requests is not installed")
    print("Run pip install -r requirements.txt before continuing")
    exit(1)

TAG_NAME = ""

def ensure_str(string):
    """
    ensure_str: Ensure strings are UTF-8 encoded
    """
    if isinstance(string, unicode):
        string = string.encode('utf-8')
    return string


FULL_NAMES = []

if len(sys.argv) == 3:
    FULL_NAMES.append(sys.argv[1] + "/" + sys.argv[2])
elif len(sys.argv) == 2:
    API_RESPONSE = requests.get('https://api.github.com/users/' + sys.argv[1] + '/repos').json()

    for rep in API_RESPONSE:
        FULL_NAMES.insert(0, ensure_str(rep['full_name']))
elif len(sys.argv) == 4:
    FULL_NAMES.append(sys.argv[1] + "/" + sys.argv[2])
    TAG_NAME = sys.argv[3]
else:
    print("Usage: " + sys.argv[0] + " github-user [github-project]")
    exit(1)

for full_name in FULL_NAMES:
    buf = io.StringIO()
    try:
        API_RESPONSE = requests.get('https://api.github.com/repos/' + full_name + '/releases').json()

        for p in API_RESPONSE:
            print("\n")
            if "assets" in p:
                print("Tag: " + p['tag_name'] + ", Created on " + p['created_at'].split('T')[0])
                for asset in p['assets']:
                    if len(TAG_NAME) == 0 or p['tag_name'] != TAG_NAME:
                        print(asset['name'] + ", Downloaded "
                              + str(asset['download_count']) + " times")
                    else:
                        if p['tag_name'] == TAG_NAME:
                            print(asset['name'] + ", Downloaded "
                                  + str(asset['download_count']) + " times")
                            exit(2)
            else:
                print("No data")
    except KeyError:
        pass
