#!/usr/bin/env python3

import sys
import io

from future.types.newstr import unicode

tag_name = ""
try:
    import requests
except ImportError:
    print("Error: requests is not installed")
    print("Run pip install -r requirements.txt before continuing")
    exit(1)


def ensure_str(s):
    if isinstance(s, unicode):
        s = s.encode('utf-8')
    return s


full_names = []

if len(sys.argv) == 3:
    full_names.append(sys.argv[1] + "/" + sys.argv[2])
elif len(sys.argv) == 2:
    r = requests.get('https://api.github.com/users/' + sys.argv[1] + '/repos')
    myobj = r.json()

    for rep in myobj:
        full_names.insert(0, ensure_str(rep['full_name']))
elif len(sys.argv) == 4:
    full_names.append(sys.argv[1] + "/" + sys.argv[2])
    tag_name = sys.argv[3]
else:
    print("Usage: " + sys.argv[0] + " github-user [github-project]")
    exit(1)

for full_name in full_names:
    buf = io.StringIO()
    try:
        r = requests.get('https://api.github.com/repos/' + full_name + '/releases')
        myobj = r.json()

        for p in myobj:
            print("\n")
            if "assets" in p:
                print("Tag: " + p['tag_name'] + ", Created on " + p['created_at'].split('T')[0])
                for asset in p['assets']:
                    if len(tag_name) == 0 or p['tag_name'] != tag_name:
                        print(asset['name'] + ", Downloaded " + str(asset['download_count']) + " times")
                    else:
                        if p['tag_name'] == tag_name:
                            print(asset['name'] + ", Downloaded " + str(asset['download_count']) + " times")
                            exit(2)
            else:
                print("No data")
    except:
        pass
